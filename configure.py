import glob, os, sys
import sipconfig

if __name__=="__main__":
    inc_dir="src"
    lib_dir="src\\release"
    dest_pkg_dir="testobject"
    
    config=sipconfig.Configuration()
    
    sip_files_dir="sip"      
    output_dir="modules"
    if not os.path.exists(output_dir): os.mkdir(output_dir)

    build_file="testobject.sbf"
    build_path=os.path.join(output_dir, build_file)   
    sip_file=os.path.join("sip", "PyTestObject.sip")
    
    command=" ".join([
        config.sip_bin,
        "-c", output_dir,
        "-b", build_path,
        "-I"+config.sip_inc_dir,
        "-I"+inc_dir,
        "-I/usr/include",
        "-Isip",
        "-w",
        "-o",
        sip_file
    ])
    sys.stdout.write(command+"\n")
    sys.stdout.flush()
    
    if os.system(command) != 0:
        sys.exit(1)
    
    makefile=sipconfig.ModuleMakefile(
        config,
        build_file,
        dir=output_dir,
        install_dir=dest_pkg_dir
    )
    
    makefile.extra_include_dirs+=[os.path.abspath(inc_dir)]
    makefile.extra_lib_dirs+=[os.path.abspath(lib_dir)]
    makefile.extra_lflags+=["-Wl,-rpath="+os.path.abspath("src")]
    makefile.extra_libs+=["testobject"]   
    makefile.generate()
    
    sipconfig.ParentMakefile(
        configuration=config,
        subdirs=["src", output_dir],
        ).generate()
    
    os.chdir("src")
    os.system("qmake")   
    sys.exit()