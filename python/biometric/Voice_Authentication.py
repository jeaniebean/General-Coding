from __future__ import division
import os
import shutil
from math import sqrt, fsum
from random import uniform, sample, shuffle
from collections import defaultdict

# Voice Authentication using wave signature files and given enrollment samples

def verify(sig_dir, wav_dir, dest_dir, src_data, dest_data):
	src_size, tgt_size, n, sig_size = 5, 50, 2, 20
	src_files, tgt_files = [], []	
	
	def extract_files():			# Extract list f files of the given directory
		with open(src_data, 'r') as f:
			for line in f:
				src_files.append(line.strip())

		filelist = os.listdir(sig_dir)
		for filename in filelist:
			if filename not in src_files:
				tgt_files.append(filename)

	def gen_vector(files):			# Based on given file, generate vector for file signatures
		vector = defaultdict(list)
		for f in files:
			filename = sig_dir + f
			with open(filename, 'r') as inFile:
				header = inFile.readline()
				for i in xrange(sig_size):
					line = inFile.readline()
					vector[f].append( float(line.strip()) )
		return vector

	def derive_SD(t_vtr):
		m_vtr,  m_avg, mean = {}, [0]*sig_size, 0

		for t in t_vtr:				# Derive random vector based on range of min/max of original vector												
			_min, _max = min(t_vtr[t]), max (t_vtr[t])
			rand_vtr = [uniform(_min, _max) for x in xrange(sig_size)]
			m_vtr[t] = [(v+r) for (v,r) in zip(t_vtr[t], rand_vtr)]

		for m in m_vtr:				# Calculate mean vector based on 2 enrollment sample
			m_avg = [(m_i + m_j) for (m_i, m_j) in zip(m_vtr[m], m_avg)]
		m_avg = [m/n for m in m_avg]

		for m in m_vtr:				# Calculate standard deviation
			_diff = [(m_i - m_j)**2 for (m_i, m_j) in zip(m_vtr[m], m_avg)]
			mean = mean + sum(_diff)
		std_dev = sqrt(mean) / n
		return std_dev

	def euclid_dist(r_vector, s_vector):
		final_vector = [(r-s)**2 for (r, s) in zip(r_vector, s_vector)]
		distance = sqrt( fsum(final_vector) )
		return distance

	def output(result_list):
		lines = {}

		return lines

	# Extract data, shuffle source and target sample, generate 20x1 vector, 
	extract_files()
	shuffle(src_files)
	selected_tgt = sample(tgt_files, tgt_size)
	src_vtr = gen_vector(src_files)
	tgt_vtr = gen_vector(selected_tgt)

	t_vtr = {t:src_vtr[t] for t in src_files[:n]}
	r_src, r_vtr = src_files[n], src_vtr[src_files[n]]
	__vtr = {t:src_vtr[t] for t in src_files[n+1:]}
	tgt_vtr.update(__vtr) 
	std_dev, delta = derive_SD(t_vtr), 0.001
	wav_list = set()
	with open(dest_data, 'wt') as outFile:
		for i in xrange(-5, 6, 1):
			result_list = defaultdict(int)
			curr_std_dev = std_dev + i*delta
			out = 'Standard Deviation : ' + str(std_dev) + '\tDelta : ' + str(i*delta) + '\n'
			outFile.write(out)

			for tgt in tgt_vtr:
				dist = euclid_dist(r_vtr, tgt_vtr[tgt])
				r = dist <= curr_std_dev
				if tgt in src_files:
					expected, result = 'TA', 'TA' if r else 'FR'
				else:
					expected, result = 'TR', 'FA' if r else 'TR'
				result_list[result] += 1
				out = r_src + ', ' + tgt + ', ' + str(dist) + ', ' + expected + ', ' + result + '\n'
				wav_list.add(tgt.replace('signature', 'wav'))
				outFile.write(out)

			TA, FR, TR, FA = result_list['TA'], result_list['FR'], result_list['TR'], result_list['FA']
			FAR, FRR = FA / (FA + TR), FR / (FR + TA)
			outFile.write('TA : ' + str(TA) + '\tFR : ' + str(FR) + '\n')
			outFile.write('TR : '+ str(TR) + '\tFA : ' + str(FA)  + '\n')
			outFile.write('FAR : '+ str(FAR) + '\tFRR : ' + str(FRR) + '\n\n')

	os.mkdir(dest_dir)
	for wav in wav_list:
		shutil.copy(os.path.join(wav_dir + wav), dest_dir)
	shutil.copy(dest_data, dest_dir)

def main():
	root = 'd:\\'
	sig_dir = os.path.join(root + 'SIG\\') 
	wav_dir = os.path.join(root + 'WAV\\')
	dest_dir = os.path.join(root + 'SAMPLE')
	src, dest = 'enrollment_data.txt', 'verified_signature.txt'
	src_data, out_data= os.path.join(root + src), os.path.join(root + dest)
	verify(sig_dir, wav_dir, dest_dir, src_data, out_data)

if __name__ == "__main__":
	main()