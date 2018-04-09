#!/Users/alexaubrey/anaconda/envs/msds5013/bin/python

redteam_src_hosts = ["C17693","C18025","C19932","C22409"]

#redteam_dest_hosts = ["C1","C10","C10005","C1003","C1006","C1014","C1015","C102","C1022","C1028","C10405","C1042","C1046","C10577","C1065","C108","C10817","C1085","C1089","C1096","C11039","C11178","C1119","C11194","C1124","C1125","C113","C115","C11727","C1173","C1183","C1191","C12116","C1215","C1222","C1224","C12320","C12448","C12512","C126","C1268","C12682","C1269","C1275","C1302","C1319","C13713","C1382","C1415","C143","C1432","C1438","C1448","C1461","C1477","C1479","C148","C1482","C1484","C1493","C15","C1500","C1503","C1506","C1509","C15197","C152","C15232","C1549","C155","C1555","C1567","C1570","C1581","C16088","C1610","C1611","C1616","C1626","C1632","C16401","C16467","C16563","C1710","C1732","C1737","C17425","C17600","C17636","C17640","C177","C1776","C17776","C17806","C1784","C17860","C1797","C1810","C18113","C18190","C1823","C18464","C18626","C1887","C18872","C19038","C1906","C19156","C19356","C1936","C1944","C19444","C1952","C1961","C1964","C1966","C1980","C19803","C2012","C2013","C20203","C20455","C2057","C2058","C20677","C2079","C20819","C2085","C2091","C20966","C21349","C21664","C21814","C21919","C21946","C2196","C21963","C22174","C22176","C22275","C2254","C22766","C231","C2341","C2378","C2388","C243","C246","C2519","C2578","C2597","C2604","C2609","C2648","C2669","C2725","C2816","C2844","C2846","C2849","C2877","C2914","C294","C2944","C3019","C302","C3037","C305","C306","C307","C313","C3153","C3170","C3173","C3199","C3249","C3288","C3292","C3303","C3305","C332","C338","C3380","C3388","C3422","C3435","C3437","C3455","C346","C3491","C3521","C353","C3586","C359","C3597","C3601","C3610","C3629","C3635","C366","C368","C3699","C370","C3755","C3758","C3813","C385","C3888","C395","C398","C400","C4106","C4159","C4161","C42","C423","C4280","C429","C430","C4403","C452","C4554","C457","C458","C46","C4610","C464","C467","C477","C4773","C4845","C486","C492","C4934","C5030","C504","C506","C5111","C513","C52","C528","C529","C5343","C5439","C5453","C553","C5618","C5653","C5693","C583","C586","C61","C612","C625","C626","C633","C636","C6487","C6513","C685","C687","C706","C7131","C721","C728","C742","C7464","C7503","C754","C7597","C765","C7782","C779","C78","C791","C798","C801","C8172","C8209","C828","C849","C8490","C853","C8585","C8751","C881","C882","C883","C886","C89","C90","C9006","C917","C92","C923","C96","C965","C9692","C9723","C977","C9945"]
redteam_dest_hosts = ["C1","C10","C10005","C1003","C1006","C1014","C1015","C102","C1022","C1028","C10405","C1042","C1046","C10577","C1065","C108","C10817","C1085","C1089","C1096","C11039","C11178","C1119","C11194","C1124","C1125","C113","C115","C11727","C1173","C1183","C1191","C12116","C1215","C1222","C1224","C12320","C12448","C12512","C126","C1268","C12682","C1269"]

#outfile = open('auth_filtered_only_redteam_lines.txt', 'w')
outfile = open('auth_filtered_only_non_redteam_lines.txt', 'w')
for line in open('auth_filtered.txt', 'r'):
	src_hostname = line.split(",")[3].strip()
	dest_hostname = line.split(",")[4].strip()

	#if src_hostname in redteam_src_hosts or src_hostname in redteam_dest_hosts:
	if not src_hostname in redteam_src_hosts and not src_hostname in redteam_dest_hosts:
		outfile.write(line)
outfile.close()
