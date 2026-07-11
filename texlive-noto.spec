%global tl_name noto
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for Noto fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/noto
License:	lppl ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the NotoSerif, NotoSans and NotoSansMono families of fonts, designed by
Steve Matteson for Google.

