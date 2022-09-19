#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fltk
Version  : 1.3.8
Release  : 11
URL      : https://www.fltk.org/pub/fltk/1.3.8/fltk-1.3.8-source.tar.gz
Source0  : https://www.fltk.org/pub/fltk/1.3.8/fltk-1.3.8-source.tar.gz
Summary  : Fast Light Tool Kit (FLTK)
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 Libpng MIT
Requires: fltk-bin = %{version}-%{release}
Requires: fltk-lib = %{version}-%{release}
Requires: fltk-license = %{version}-%{release}
Requires: fltk-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : freetype-dev
BuildRequires : glu-dev
BuildRequires : groff
BuildRequires : libXcursor-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(xft)
Patch1: fltk-config-dynlibs.patch

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a
cross-platform C++ GUI toolkit for UNIX(r)/Linux(r) (X11),
Microsoft(r) Windows(r), and MacOS(r) X.  FLTK provides modern
GUI functionality without the bloat and supports 3D graphics via
OpenGL(r) and its built-in GLUT emulation.

%package bin
Summary: bin components for the fltk package.
Group: Binaries
Requires: fltk-license = %{version}-%{release}

%description bin
bin components for the fltk package.


%package dev
Summary: dev components for the fltk package.
Group: Development
Requires: fltk-lib = %{version}-%{release}
Requires: fltk-bin = %{version}-%{release}
Provides: fltk-devel = %{version}-%{release}
Requires: fltk = %{version}-%{release}

%description dev
dev components for the fltk package.


%package doc
Summary: doc components for the fltk package.
Group: Documentation
Requires: fltk-man = %{version}-%{release}

%description doc
doc components for the fltk package.


%package lib
Summary: lib components for the fltk package.
Group: Libraries
Requires: fltk-license = %{version}-%{release}

%description lib
lib components for the fltk package.


%package license
Summary: license components for the fltk package.
Group: Default

%description license
license components for the fltk package.


%package man
Summary: man components for the fltk package.
Group: Default

%description man
man components for the fltk package.


%prep
%setup -q -n fltk-1.3.8
cd %{_builddir}/fltk-1.3.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663618569
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --enable-threads \
--enable-xft \
--enable-shared
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1663618569
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fltk
cp %{_builddir}/fltk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/fltk/804b2d61c0867ff1b0b0cb5648970d5aba808713
cp %{_builddir}/fltk-%{version}/documentation/src/license.dox %{buildroot}/usr/share/package-licenses/fltk/ed64c0250faa1fc40311e0bf1a2f4fba654beaad
cp %{_builddir}/fltk-%{version}/png/LICENSE %{buildroot}/usr/share/package-licenses/fltk/fc3951ba26fe1914759f605696a1d23e3b41766f
cp %{_builddir}/fltk-%{version}/src/xutf8/COPYING %{buildroot}/usr/share/package-licenses/fltk/93fd5552183411097c82fa6032cab1142ae7887b
cp %{_builddir}/fltk-%{version}/src/xutf8/lcUniConv/COPYRIGHT %{buildroot}/usr/share/package-licenses/fltk/d9fcea34224bf0b199bd29e6f25d0280f5e05ca8
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fltk-config
/usr/bin/fluid

%files dev
%defattr(-,root,root,-)
/usr/include/FL/Enumerations.H
/usr/include/FL/Fl.H
/usr/include/FL/Fl_Adjuster.H
/usr/include/FL/Fl_BMP_Image.H
/usr/include/FL/Fl_Bitmap.H
/usr/include/FL/Fl_Box.H
/usr/include/FL/Fl_Browser.H
/usr/include/FL/Fl_Browser_.H
/usr/include/FL/Fl_Button.H
/usr/include/FL/Fl_Cairo.H
/usr/include/FL/Fl_Cairo_Window.H
/usr/include/FL/Fl_Chart.H
/usr/include/FL/Fl_Check_Browser.H
/usr/include/FL/Fl_Check_Button.H
/usr/include/FL/Fl_Choice.H
/usr/include/FL/Fl_Clock.H
/usr/include/FL/Fl_Color_Chooser.H
/usr/include/FL/Fl_Copy_Surface.H
/usr/include/FL/Fl_Counter.H
/usr/include/FL/Fl_Device.H
/usr/include/FL/Fl_Dial.H
/usr/include/FL/Fl_Double_Window.H
/usr/include/FL/Fl_Export.H
/usr/include/FL/Fl_File_Browser.H
/usr/include/FL/Fl_File_Chooser.H
/usr/include/FL/Fl_File_Icon.H
/usr/include/FL/Fl_File_Input.H
/usr/include/FL/Fl_Fill_Dial.H
/usr/include/FL/Fl_Fill_Slider.H
/usr/include/FL/Fl_Float_Input.H
/usr/include/FL/Fl_FormsBitmap.H
/usr/include/FL/Fl_FormsPixmap.H
/usr/include/FL/Fl_Free.H
/usr/include/FL/Fl_GIF_Image.H
/usr/include/FL/Fl_Gl_Window.H
/usr/include/FL/Fl_Group.H
/usr/include/FL/Fl_Help_Dialog.H
/usr/include/FL/Fl_Help_View.H
/usr/include/FL/Fl_Hold_Browser.H
/usr/include/FL/Fl_Hor_Fill_Slider.H
/usr/include/FL/Fl_Hor_Nice_Slider.H
/usr/include/FL/Fl_Hor_Slider.H
/usr/include/FL/Fl_Hor_Value_Slider.H
/usr/include/FL/Fl_Image.H
/usr/include/FL/Fl_Image_Surface.H
/usr/include/FL/Fl_Input.H
/usr/include/FL/Fl_Input_.H
/usr/include/FL/Fl_Input_Choice.H
/usr/include/FL/Fl_Int_Input.H
/usr/include/FL/Fl_JPEG_Image.H
/usr/include/FL/Fl_Light_Button.H
/usr/include/FL/Fl_Line_Dial.H
/usr/include/FL/Fl_Menu.H
/usr/include/FL/Fl_Menu_.H
/usr/include/FL/Fl_Menu_Bar.H
/usr/include/FL/Fl_Menu_Button.H
/usr/include/FL/Fl_Menu_Item.H
/usr/include/FL/Fl_Menu_Window.H
/usr/include/FL/Fl_Multi_Browser.H
/usr/include/FL/Fl_Multi_Label.H
/usr/include/FL/Fl_Multiline_Input.H
/usr/include/FL/Fl_Multiline_Output.H
/usr/include/FL/Fl_Native_File_Chooser.H
/usr/include/FL/Fl_Nice_Slider.H
/usr/include/FL/Fl_Object.H
/usr/include/FL/Fl_Output.H
/usr/include/FL/Fl_Overlay_Window.H
/usr/include/FL/Fl_PNG_Image.H
/usr/include/FL/Fl_PNM_Image.H
/usr/include/FL/Fl_Pack.H
/usr/include/FL/Fl_Paged_Device.H
/usr/include/FL/Fl_Pixmap.H
/usr/include/FL/Fl_Plugin.H
/usr/include/FL/Fl_Positioner.H
/usr/include/FL/Fl_PostScript.H
/usr/include/FL/Fl_Preferences.H
/usr/include/FL/Fl_Printer.H
/usr/include/FL/Fl_Progress.H
/usr/include/FL/Fl_RGB_Image.H
/usr/include/FL/Fl_Radio_Button.H
/usr/include/FL/Fl_Radio_Light_Button.H
/usr/include/FL/Fl_Radio_Round_Button.H
/usr/include/FL/Fl_Repeat_Button.H
/usr/include/FL/Fl_Return_Button.H
/usr/include/FL/Fl_Roller.H
/usr/include/FL/Fl_Round_Button.H
/usr/include/FL/Fl_Round_Clock.H
/usr/include/FL/Fl_Scroll.H
/usr/include/FL/Fl_Scrollbar.H
/usr/include/FL/Fl_Secret_Input.H
/usr/include/FL/Fl_Select_Browser.H
/usr/include/FL/Fl_Shared_Image.H
/usr/include/FL/Fl_Simple_Counter.H
/usr/include/FL/Fl_Single_Window.H
/usr/include/FL/Fl_Slider.H
/usr/include/FL/Fl_Spinner.H
/usr/include/FL/Fl_Sys_Menu_Bar.H
/usr/include/FL/Fl_Table.H
/usr/include/FL/Fl_Table_Row.H
/usr/include/FL/Fl_Tabs.H
/usr/include/FL/Fl_Text_Buffer.H
/usr/include/FL/Fl_Text_Display.H
/usr/include/FL/Fl_Text_Editor.H
/usr/include/FL/Fl_Tile.H
/usr/include/FL/Fl_Tiled_Image.H
/usr/include/FL/Fl_Timer.H
/usr/include/FL/Fl_Toggle_Button.H
/usr/include/FL/Fl_Toggle_Light_Button.H
/usr/include/FL/Fl_Toggle_Round_Button.H
/usr/include/FL/Fl_Tooltip.H
/usr/include/FL/Fl_Tree.H
/usr/include/FL/Fl_Tree_Item.H
/usr/include/FL/Fl_Tree_Item_Array.H
/usr/include/FL/Fl_Tree_Prefs.H
/usr/include/FL/Fl_Valuator.H
/usr/include/FL/Fl_Value_Input.H
/usr/include/FL/Fl_Value_Output.H
/usr/include/FL/Fl_Value_Slider.H
/usr/include/FL/Fl_Widget.H
/usr/include/FL/Fl_Window.H
/usr/include/FL/Fl_Wizard.H
/usr/include/FL/Fl_XBM_Image.H
/usr/include/FL/Fl_XPM_Image.H
/usr/include/FL/abi-version.h
/usr/include/FL/dirent.h
/usr/include/FL/filename.H
/usr/include/FL/fl_ask.H
/usr/include/FL/fl_draw.H
/usr/include/FL/fl_message.H
/usr/include/FL/fl_show_colormap.H
/usr/include/FL/fl_show_input.H
/usr/include/FL/fl_types.h
/usr/include/FL/fl_utf8.h
/usr/include/FL/forms.H
/usr/include/FL/gl.h
/usr/include/FL/gl2opengl.h
/usr/include/FL/gl_draw.H
/usr/include/FL/glu.h
/usr/include/FL/glut.H
/usr/include/FL/mac.H
/usr/include/FL/math.h
/usr/include/FL/names.h
/usr/include/FL/platform.H
/usr/include/FL/win32.H
/usr/include/FL/x.H
/usr/lib64/libfltk.so
/usr/lib64/libfltk_forms.so
/usr/lib64/libfltk_gl.so
/usr/lib64/libfltk_images.so
/usr/share/man/man3/fltk.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/fltk/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfltk.so.1.3
/usr/lib64/libfltk_forms.so.1.3
/usr/lib64/libfltk_gl.so.1.3
/usr/lib64/libfltk_images.so.1.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fltk/804b2d61c0867ff1b0b0cb5648970d5aba808713
/usr/share/package-licenses/fltk/93fd5552183411097c82fa6032cab1142ae7887b
/usr/share/package-licenses/fltk/d9fcea34224bf0b199bd29e6f25d0280f5e05ca8
/usr/share/package-licenses/fltk/ed64c0250faa1fc40311e0bf1a2f4fba654beaad
/usr/share/package-licenses/fltk/fc3951ba26fe1914759f605696a1d23e3b41766f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/cat1/fltk-config.1
/usr/share/man/cat1/fluid.1
/usr/share/man/cat3/fltk.3
/usr/share/man/man1/fltk-config.1
/usr/share/man/man1/fluid.1
