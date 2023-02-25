

import ipaddress as ip
import nettoolkit as nt


def str_to_list(item):
	"""splits string and returns list, items separated by either `comma`, `enter` 
	--> list
	"""
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
	"""joins provided items (iterables) by `spaces`
	--> string
	"""
	return " ".join(items)

def comma_separated(items):
	"""joins provided items (iterables) by `comma`
	--> string
	"""
	return ",".join(items)

def list_append(lst, item):
	"""append an item to list
	--> list
	"""
	return lst.append(item)

def list_extend(lst, item):
	"""Extend the list of items to list
	--> list
	"""
	return lst.extend(item)

def list_sorted(lst):
	"""provided sorted elements in list
	--> list
	"""
	return sorted(lst)

def convert_to_int(lst):
	"""convert numeric string type elements to integer type in a list.
	--> list
	"""
	return [ int(x) for x in lst]

def groups_of_nine(lst):
	"""breaks down provided list in to multiple groups with max. nine elements in each group
	--> list of lists
	"""
	# lst = np.int16(np.array(lst))
	lst = nt.LST.convert_vlans_list_to_range_of_vlans_list(lst)
	lst = [ str(_) for _ in lst ]
	return nt.LST.split(lst, 9)	

def physical_if_allowed(vlan, table):
	"""condition: checks for `filter==physical` and `vlan in vlan_members`
	--> interface value of matching row
	"""
	for key, data in table.items():
		if data['filter'].lower()=='physical' and int(vlan) in nt.LST.expand_vlan_list(str_to_list(data['vlan_members'])):
			return data['interface']
	return ""

def remove_trailing_zeros(net):
	"""removes the trailing zeros from given ipv6 address
	--> str
	"""
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

def nth_ip(net, n, withMask=False):
	"""get n-th ip address of given network.
	withMask: will return value along with mask else only subnet 
	"""
	_net = str(ip.ip_interface(net).network)
	v4 = nt.addressing(_net)
	return v4.n_thIP(n, True) if withMask else v4[n]

def mask(net):
	"""get the subnet mask for given network
	eg: 24
	"""
	_net = str(ip.ip_interface(net).network)
	v4 = nt.addressing(_net)
	return v4.mask

def netmask(net):
	"""get network mask for given network
	eg. 255.255.255.0
	"""
	return str(ip.ip_interface(net).netmask)

def invmask(net):
	"""get inverse mask for given network
	eg. 0.0.0.255
	"""
	v4 = v4addressing(net)
	return str(v4.invmask)

def addressing(net): 
	"""get the ip of given subnet
	"""
	return ip.ip_interface(net)

def int_to_str(data):
	"""get the actual physical interface value by removing training sub interfaces.
	"""
	return str(data).split(".")[0]

def v4addressing(ip, mask="32"):
	"""get the IPv4 objetct for given ip, mask (default mask=32)
	--> IPv4
	"""
	if ip.find("/") > 0: return nt.IPv4(ip)
	return nt.IPv4(ip+"/"+str(mask))

def get_summaries(lst_of_pfxs):
	"""get the summaries for provided prefixes.
	--> list
	"""
	lst_of_pfxs = nt.LST.remove_empty_members(lst_of_pfxs)
	try:
		return nt.get_summaries(*lst_of_pfxs)
	except:
		print(f"ERROR RECEIVE SUMMARIES {lst_of_pfxs}")
		return []

def iprint(x): 
	"""i print function to be use withing jinja template for debug.
	"""
	print(x)

def get_item(lst, n):
	"""get the nth item from list

	Args:
		lst (list): list containing various items
		n (int): index of item to be retrived 

	Returns:
		str: n-th item from list
	"""
	try:
		if isinstance(lst, (list, tuple)):
			return lst[n]
		else:
			return lst
	except:
		return lst
