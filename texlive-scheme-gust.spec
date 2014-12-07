# revision 30372
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-gust
Version:	20131013
Release:	8
Summary:	GUST TeX Live scheme
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-gust.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-FAQ-en
Requires:	texlive-Type1fonts
Requires:	texlive-amslatex-primer
Requires:	texlive-amstex
Requires:	texlive-antt
Requires:	texlive-bibtex8
Requires:	texlive-comment
Requires:	texlive-comprehensive
Requires:	texlive-concrete
Requires:	texlive-cyklop
Requires:	texlive-dvidvi
Requires:	texlive-dviljk
Requires:	texlive-gustprog
Requires:	texlive-impatient
Requires:	texlive-iwona
Requires:	texlive-metafont-beginners
Requires:	texlive-metapost-examples
Requires:	texlive-poltawski
Requires:	texlive-seetexk
Requires:	texlive-seminar
Requires:	texlive-tds
Requires:	texlive-tex4ht
Requires:	texlive-texdoc
Requires:	texlive-collection-basic
Requires:	texlive-collection-context
Requires:	texlive-collection-fontutils
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-genericrecommended
Requires:	texlive-collection-langpolish
Requires:	texlive-collection-latex
Requires:	texlive-collection-latexrecommended
Requires:	texlive-collection-metapost
Requires:	texlive-collection-xetex

%description
This is the GUST TeX Live scheme: it is a set of files
sufficient to typeset Polish plain TeX, LaTeX and ConTeXt
documents in PostScript or PDF.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
