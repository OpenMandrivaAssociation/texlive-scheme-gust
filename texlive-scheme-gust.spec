%global tl_name scheme-gust
%global tl_revision 59755

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	GUST TeX Live scheme
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-gust
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-gust.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amslatex-primer)
Requires:	texlive(amstex)
Requires:	texlive(antt)
Requires:	texlive(bibtex8)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-context)
Requires:	texlive(collection-fontsrecommended)
Requires:	texlive(collection-fontutils)
Requires:	texlive(collection-langpolish)
Requires:	texlive(collection-latex)
Requires:	texlive(collection-latexrecommended)
Requires:	texlive(collection-metapost)
Requires:	texlive(collection-plaingeneric)
Requires:	texlive(collection-texworks)
Requires:	texlive(collection-xetex)
Requires:	texlive(comment)
Requires:	texlive(comprehensive)
Requires:	texlive(concrete)
Requires:	texlive(cyklop)
Requires:	texlive(dvidvi)
Requires:	texlive(dviljk)
Requires:	texlive(fontinstallationguide)
Requires:	texlive(gustprog)
Requires:	texlive(impatient)
Requires:	texlive(iwona)
Requires:	texlive(metafont-beginners)
Requires:	texlive(metapost-examples)
Requires:	texlive(poltawski)
Requires:	texlive(seetexk)
Requires:	texlive(seminar)
Requires:	texlive(tds)
Requires:	texlive(tex4ht)
Requires:	texlive(texdoc)
Provides:	texlive(%{tl_name}) = %{version}

%description
This is the GUST TeX Live scheme: it is a set of files sufficient to
typeset Polish plain TeX, LaTeX and ConTeXt documents in PostScript or
PDF.

