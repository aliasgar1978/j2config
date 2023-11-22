
Version Control
=================================================



.. list-table:: Version Control updates
   :widths: 10 15 200
   :header-rows: 1

   * - version
     - date   
     - Updates

   * - 0.0.1
     - Jan 15, 2023
     - Initial release on pypi 
   * - 0.0.2
     - Jan 29, 2023
     - doc update
   * - 0.0.3
     - Feb 25, 2023
     - untracked
   * - 0.0.4
     - Mar 22, 2023
     - untracked
   * - 0.0.5
     - Mar 23, 2023
     - Bug fix to support older version python 3.9, since python<3.10 does not support staticmethod call. 
   * - 0.0.6
     - Jul 16, 2023
     - * Removed `custom global file` read and `processing` from standard implementation. 
       * Added a hook **ABSRegion** class in order to support it via custom implementation.  
       * Input variable **global_file** for PrepareConfig class changed to **regional_file**.
       * New variable **regional_class** added for PrepareConfig class in order to process custom *regional_class* along with custom *regional_file*.
   * - 0.1.1
     - Nov 1, 2023
     - added **OSPF** and **STATIC ROUTES** filters. 



.. warning::

  * Updation of this package individually is stopped.
  * Package is incorporated in ``nettoolkit`` package as a sub-package.
  * Use nettoolkit for the future updates.

-----


.. note::

   some of version updates were untracked.

