
Using j2config along with custom class, modules
===================================================

Apart from usual previous steps, we can add the custom classes, modules to be accessible over jinja templates.  

Refer below details on how to use them.

full module import should declare pure methods only.  Classes should be imported explicitely from diverse modules.

Detailed How To
---------------------

	#. Import necessary custom class(es) from module, and/or import necessary module(s).

		**Below depicts a Sample Code.** 
		Modify it as per your custom class(es) requirements.

		.. code::

			from custom_j2config.classes import Summaries, Vrf, Vlan, Bgp, Physical
			from custom_j2config import module1


	#. Include all imported classes and modules in to a dictionary and set respectively as given sample below.

		.. code::

			custom_classes = {
				'Summaries': Summaries,
				'Vrf': Vrf,
				'Vlan': Vlan,
				'Bgp': Bgp,
				'Physical': Physical
				### add all impored classes here ###
			}
			custom_modules = {module1, }  ### add all imported modules here ###


	#. Insert custom class meta data to PrepareConfig instance filters (created in previous step)

		.. code:: python

			### From previous step ###
			PrCfg = PrepareConfig(data_file, jtemplate_file, output_folder, global_variables_file)

			### Add below two additional steps to include custom class/module methods as filter to jinja processsing.
			### 1. Add Custom classes to above instance using `custom_class_add_to_filter`.
			PrCfg.custom_class_add_to_filter(**custom_classes)

			### 2. Add Custom modules to above instance using `custom_module_methods_add_to_filter`.
			PrCfg.custom_module_methods_add_to_filter(*custom_modules)

			#### Start configration Generation
			PrCfg.start()




.. note:: Congratulations!!!

	Hurrey!!! Now you can access custom declared classes/methods from within jinja template. 



.. admonition:: Notice

	Make a note that output generates based on jinja template and template variables.		

	It is soleley users responsiblity for providing appropriate filters as ``custom_classes`` and ``custom_modules``, as well as using those in `jinja templates`.

	Make sure to cross-check the generated facts before using it.

