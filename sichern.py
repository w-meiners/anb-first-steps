def copy_files_to_destination(*src, dest='.', create_dest=True, follow_symlinks=True):
    ''' copy files to dest where
        *src is the list of files
        dest is a directory
        
        example:
        >>> # a/b, a/c are existing files, 
        >>> # b is not existing path
        >>> copy_files_to_destination('a/b','a/c', dest='b')
        Pfad 'b' angelegt
        Datei 'a/b' nach 'b' kopiert
        Datei 'a/c' nach 'b' kopiert
    '''
    import os, shutil as su
    
    if not os.path.exists(dest):
        if not create_dest:
            raise Exception(f"Pfad '{dest}' existiert nicht")

        try:
            os.mkdir(dest)
            print(f"Pfad '{dest}' angelegt")
        except:
            raise Exception(f"Pfad '{dest}' konnte nicht angelegt werden")

    else: # dest exists, but is it a path
        if not os.path.isdir(dest):
            raise Exception(f"'{dest}' ist kein Directory")
            
    # dest exists and is a dir
    missing_files_list = []
    existing_dest_files_list = []
    for s in src:
        if not os.path.isfile(s):
            missing_files_list.append(s)
        else:
            if os.path.exists(os.path.join(dest,os.path.basename(s))):
                existing_dest_files_list.append(os.path.join(dest,os.path.basename(s)))
            else:
                su.copy(s,dest,follow_symlinks=follow_symlinks)
                print(f"Datei '{s}' nach '{dest}' kopiert")
    
    for s in missing_files_list:
        print(f"'{s}' ist keine Datei")
        
    print()
        
    for s in existing_dest_files_list:
        print(f"Datei '{s}' existiert bereits")
