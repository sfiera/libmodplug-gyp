{ "targets":
  [ { "target_name": "libmodplug"
    , "product_prefix": ""
    , "type": "static_library"
    , "sources":
      [ "libmodplug-0.8.8.4/src/fastmix.cpp"
      , "libmodplug-0.8.8.4/src/load_669.cpp"
      , "libmodplug-0.8.8.4/src/load_abc.cpp"
      , "libmodplug-0.8.8.4/src/load_amf.cpp"
      , "libmodplug-0.8.8.4/src/load_ams.cpp"
      , "libmodplug-0.8.8.4/src/load_dbm.cpp"
      , "libmodplug-0.8.8.4/src/load_dmf.cpp"
      , "libmodplug-0.8.8.4/src/load_dsm.cpp"
      , "libmodplug-0.8.8.4/src/load_far.cpp"
      , "libmodplug-0.8.8.4/src/load_it.cpp"
      , "libmodplug-0.8.8.4/src/load_j2b.cpp"
      , "libmodplug-0.8.8.4/src/load_mdl.cpp"
      , "libmodplug-0.8.8.4/src/load_med.cpp"
      , "libmodplug-0.8.8.4/src/load_mid.cpp"
      , "libmodplug-0.8.8.4/src/load_mod.cpp"
      , "libmodplug-0.8.8.4/src/load_mt2.cpp"
      , "libmodplug-0.8.8.4/src/load_mtm.cpp"
      , "libmodplug-0.8.8.4/src/load_okt.cpp"
      , "libmodplug-0.8.8.4/src/load_pat.cpp"
      , "libmodplug-0.8.8.4/src/load_psm.cpp"
      , "libmodplug-0.8.8.4/src/load_ptm.cpp"
      , "libmodplug-0.8.8.4/src/load_s3m.cpp"
      , "libmodplug-0.8.8.4/src/load_stm.cpp"
      , "libmodplug-0.8.8.4/src/load_ult.cpp"
      , "libmodplug-0.8.8.4/src/load_umx.cpp"
      , "libmodplug-0.8.8.4/src/load_wav.cpp"
      , "libmodplug-0.8.8.4/src/load_xm.cpp"
      , "libmodplug-0.8.8.4/src/mmcmp.cpp"
      , "libmodplug-0.8.8.4/src/modplug.cpp"
      , "libmodplug-0.8.8.4/src/snd_dsp.cpp"
      , "libmodplug-0.8.8.4/src/snd_flt.cpp"
      , "libmodplug-0.8.8.4/src/snd_fx.cpp"
      , "libmodplug-0.8.8.4/src/sndfile.cpp"
      , "libmodplug-0.8.8.4/src/sndmix.cpp"
      ]
    , "defines": ["HAVE_CONFIG_H=1"]
    , "cxxflags":
      [ "-Wno-sizeof-pointer-memaccess"
      , "-Wno-deprecated-register"
      ]
    , "xcode_settings":
      { "WARNING_CFLAGS":
        [ "-Wno-sizeof-pointer-memaccess"
        , "-Wno-deprecated-register"
        ]
      }
    , "include_dirs":
      [ "include/darwin"
      , "libmodplug-0.8.8.4/src"
      , "libmodplug-0.8.8.4/src/libmodplug"
      ]
    , "direct_dependent_settings":
      { "include_dirs": ["include/all"]
      }
    , "conditions":
      [ [ "OS != 'mac'"
        , { "include_dirs!": ["include/darwin"]
          }
        ]
      ]
    }
  ]
}
# -*- mode: python; tab-width: 2 -*-
