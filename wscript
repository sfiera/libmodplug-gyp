# -*- mode: python -*-

def common(ctx):
    ctx.default_sdk = "10.7"
    ctx.default_compiler = "clang"
    ctx.cxx_std = "c++11"
    ctx.load("compiler_cxx")
    ctx.load("core", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)

def build(bld):
    common(bld)

    bld.stlib(
        target="libmodplug/libmodplug",
        features="universal",
        source=[
            "libmodplug-0.8.8.4/src/fastmix.cpp",
            "libmodplug-0.8.8.4/src/load_669.cpp",
            "libmodplug-0.8.8.4/src/load_abc.cpp",
            "libmodplug-0.8.8.4/src/load_amf.cpp",
            "libmodplug-0.8.8.4/src/load_ams.cpp",
            "libmodplug-0.8.8.4/src/load_dbm.cpp",
            "libmodplug-0.8.8.4/src/load_dmf.cpp",
            "libmodplug-0.8.8.4/src/load_dsm.cpp",
            "libmodplug-0.8.8.4/src/load_far.cpp",
            "libmodplug-0.8.8.4/src/load_it.cpp",
            "libmodplug-0.8.8.4/src/load_j2b.cpp",
            "libmodplug-0.8.8.4/src/load_mdl.cpp",
            "libmodplug-0.8.8.4/src/load_med.cpp",
            "libmodplug-0.8.8.4/src/load_mid.cpp",
            "libmodplug-0.8.8.4/src/load_mod.cpp",
            "libmodplug-0.8.8.4/src/load_mt2.cpp",
            "libmodplug-0.8.8.4/src/load_mtm.cpp",
            "libmodplug-0.8.8.4/src/load_okt.cpp",
            "libmodplug-0.8.8.4/src/load_pat.cpp",
            "libmodplug-0.8.8.4/src/load_psm.cpp",
            "libmodplug-0.8.8.4/src/load_ptm.cpp",
            "libmodplug-0.8.8.4/src/load_s3m.cpp",
            "libmodplug-0.8.8.4/src/load_stm.cpp",
            "libmodplug-0.8.8.4/src/load_ult.cpp",
            "libmodplug-0.8.8.4/src/load_umx.cpp",
            "libmodplug-0.8.8.4/src/load_wav.cpp",
            "libmodplug-0.8.8.4/src/load_xm.cpp",
            "libmodplug-0.8.8.4/src/mmcmp.cpp",
            "libmodplug-0.8.8.4/src/modplug.cpp",
            "libmodplug-0.8.8.4/src/snd_dsp.cpp",
            "libmodplug-0.8.8.4/src/snd_flt.cpp",
            "libmodplug-0.8.8.4/src/snd_fx.cpp",
            "libmodplug-0.8.8.4/src/sndfile.cpp",
            "libmodplug-0.8.8.4/src/sndmix.cpp",
        ],
        defines="HAVE_CONFIG_H=1",
        cflags="-Wall -Werror",
        includes=[
            "libmodplug-0.8.8.4/src",
            "libmodplug-0.8.8.4/src/libmodplug",
        ],
        export_includes="include/all",
    )

    bld.platform(
        target="libmodplug/libmodplug",
        includes="include/darwin",
        platform="darwin",
    )
