Summary:	English dictionary for /usr/share/dict
Summary(de):	Englisches Wörterbuch für /usr/share/dict
Summary(fr):	Dictionnaire anglais pour /etc/share/dict
Summary(fr):	S³ownik angielski dla /usr/share/dict
Summary(tr):	ngilizce sözlük
Name:		words
Version:	2
Release:	15
Copyright:	freeware
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://sunsite.unc.edu/pub/Linux/libs/linux.words.2.tar.gz
Patch:		linux.words-jbj.patch
Buildarch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This package contains the english dictionary in /usr/dict.  It is used by
programs like ispell as a database of words to check for spelling and so
forth.

%description -l de
Dieses Paket enthält das englische Wörterbuch in /usr/dict. Es wird von
Programmen wie ispell als Wortdatenbank, z.B. zum Prüfen der
Rechtschreibung, verwendet.

%description -l fr
Ce paquetage contient le dictionnaire anglais dans /usr/dict. Il est utilisé
par des programmes comme ispell comme base de données de mots pour vérifier
l'orthographe.

%description -l pl
W pakiecie tym znajduje siê s³ownik angielski. U¿ywany jest przez programy
takie jak ispell, kpasswd itp.

%description -l tr
Bu paket ingilizce sözlük içermektedir. Ispell gibi yazýlýmlar bu sözcük
veri tabanýný kullanarak yazým hatalarýný bulmaya çalýþýrlar.

%prep
%setup -q -c
%patch -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dict

install usr/dict/linux.words $RPM_BUILD_ROOT%{_datadir}/dict
ln -sf linux.words $RPM_BUILD_ROOT%{_datadir}/dict/words

gzip -9nf usr/dict/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc usr/dict/{README.linux.words*,README2.linux.words*}.gz

%config %verify(not size mtime md5) %{_datadir}/dict/*

%changelog
* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [2-14]
- compiled on rpm 3
- fixed gzipping %%doc

* Wed Feb 17 1999 Micha³ Kuratczyk <kura@wroclaw.art.pl>
  [2-13]
- added Group(pl)
- added gzipping documentation

* Sat Dec 19 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2-12]
- removed /usr/dict %dir from %files (this belongs to filesystems).

* Sun Nov 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- major changes.

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- take out extra.words (they're all in linux.words)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- correct desiccate (problem #794)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
