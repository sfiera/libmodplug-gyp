ifeq ($(TARGET_OS),linux)

LIBMODPLUG_CPPFLAGS := $(shell pkg-config --cflags libmodplug)
LIBMODPLUG_LDFLAGS := $(shell pkg-config --libs libmodplug)

else

LIBMODPLUG_CPPFLAGS := \
	-I $(LIBMODPLUG_ROOT)/include \
	-D MODPLUG_STATIC

LIBMODPLUG_A := $(OUT)/libmodplug.a
LIBMODPLUG_SRCS := \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/fastmix.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_669.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_abc.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_amf.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_ams.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_dbm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_dmf.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_dsm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_far.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_it.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_mdl.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_med.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_mid.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_mod.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_mt2.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_mtm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_okt.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_pat.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_psm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_ptm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_s3m.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_stm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_ult.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_umx.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_wav.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/load_xm.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/mmcmp.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/modplug.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/snd_dsp.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/snd_flt.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/snd_fx.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/sndfile.cpp \
	$(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/sndmix.cpp \

LIBMODPLUG_OBJS := $(LIBMODPLUG_SRCS:%=$(OUT)/%.o)

$(LIBMODPLUG_A): $(LIBMODPLUG_OBJS)
	$(AR) rcs $@ $+

LIBMODPLUG_PRIVATE_CPPFLAGS := \
	$(LIBMODPLUG_CPPFLAGS) \
	-I $(LIBMODPLUG_ROOT)/src/$(TARGET_OS)  \
	-I $(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src \
	-I $(LIBMODPLUG_ROOT)/libmodplug-0.8.8.5/src/libmodplug \
	-D HAVE_CONFIG_H=1  \
	-Wno-sizeof-pointer-memaccess \
	-Wno-deprecated-register \
	-Wno-macro-redefined 

$(LIBMODPLUG_OBJS): $(OUT)/%.cpp.o: %.cpp
	@$(MKDIR_P) $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(LIBMODPLUG_PRIVATE_CPPFLAGS) -c $< -o $@

-include $(LIBMODPLUG_OBJS:.o=.d)

endif
