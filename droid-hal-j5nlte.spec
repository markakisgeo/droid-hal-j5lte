# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device j5nlte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty J5

%define installable_zip 1

%define makefstab_skip_entries /dev/cpuctl /dev/stune

%define straggler_files \
/init.class_main.sh\
/init.qcom.early_boot.sh\
/init.qcom.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
/file_contexts.bin\
/property_contexts\
/sdcard\
/d\
/vendor\
/bugreports\
%{nil}

%define android_config \
#define QCOM_BSP 1\
#define QTI_BSP 1\
#define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user inet || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

