

import ipaddress as ip
import nettoolkit as nt
import numpy as np


def str_to_list(item):
	if isinstance(item, (str, int, float) ):
		items= []
		csv = item.strip().split(",")
		for _ in csv:
			lsv = _.strip().split("\n")
			for i in lsv:
				items.append(i)
		return items
	else:
		return item

def space_separated(items):
	return " ".join(items)

def comma_separated(items):
	return ",".join(items)

def list_append(lst, item):
	return lst.append(item)

def list_extend(lst, item):
	return lst.extend(item)

def list_sorted(lst):
	return sorted(lst)

def convert_to_int(lst):
	return [ int(x) for x in lst]

def groups_of_nine(lst):
	# lst = np.int16(np.array(lst))
	lst = nt.LST.convert_vlans_list_to_range_of_vlans_list(lst)
	lst = [ str(_) for _ in lst ]
	return nt.LST.split(lst, 9)	

def physical_if_allowed(vlan, table):
	for key, data in table.items():
		if data['filter'].lower()=='physical' and int(vlan) in nt.LST.expand_vlan_list(str_to_list(data['vlan_members'])):
			return data['interface']
	return ""

def remove_trailing_zeros(net):
	while True:
		trimmers = ( "::0", ":0", "::")
		exit = True
		for t in trimmers:
			if net.endswith(t):
				net = net[:-1*len(t)]
				exit = False
		if exit: break
	return net


def ipv6_urpf_acl_network(subnet):
	pfx = ip.ip_interface(subnet)
	return str(pfx.network.network_address)

def ipv6_rpf_acl_name(subnet):
	return "al6_rpf_" + remove_trailing_zeros(ipv6_urpf_acl_network(subnet))


def nth_ip(net, n, withMask=False):
	_net = str(ip.ip_interface(net).network)
	v4 = nt.addressing(_net)
	return v4.n_thIP(n, True) if withMask else v4[n]

def mask(net):
	_net = str(ip.ip_interface(net).network)
	v4 = nt.addressing(_net)
	return v4.mask

def netmask(net):
	return str(ip.ip_interface(net).netmask)

def invmask(net):
	v4 = v4addressing(net)
	return str(v4.invmask)

def addressing(net): return ip.ip_interface(net)

def int_to_str(data):
	return str(data).split(".")[0]

def v4addressing(ip, mask="32"):
	if ip.find("/") > 0: return nt.IPv4(ip)
	return nt.IPv4(ip+"/"+str(mask))

def get_summaries(lst_of_pfxs):
	lst_of_pfxs = nt.LST.remove_empty_members(lst_of_pfxs)
	try:
		return nt.get_summaries(*lst_of_pfxs)
	except:
		print(f"ERROR RECEIVE SUMMARIES {lst_of_pfxs}")
		return []

def iprint(x): print(x)

