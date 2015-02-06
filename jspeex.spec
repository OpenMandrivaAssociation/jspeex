Name:           jspeex
Version:        0.9.7
Release:        0.0.5
Summary:        100% Java Speex encoder/decoder/converter library
License:        BSD
Url:            http://jspeex.sourceforge.net/
Group:          Development/Java
Source0:        %{name}-%{version}.tar.bz2
Patch:          %{name}-build.xml
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  java-rpmbuild >= 1.5
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  junit
BuildRequires:  update-alternatives
BuildRequires:	xml-commons-apis
BuildRequires:	xml-commons-resolver
Requires:       java >= 1.5
BuildArch:      noarch

%description
JSpeex is a Java port of the Speex speech codec (Open Source/Free Software
patent-free audio compression format designed for speech).

It provides both the decoder and the encoder in pure Java, as well as a
JavaSound SPI.

%package javadoc
Summary:  Javadoc for %{name}
Group:    Development/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
%patch

dos2unix  TODO License.txt README
%__chmod 644 TODO License.txt README

%build
%ant package javadoc

%install
# jar
%__install -dm 755 %{buildroot}%{_javadir}
%__install -m 644 dist/%{name}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

# startscripts
%__cat > %{name}_enc.sh << EOF
#!/bin/bash
%{java} -jar %{_javadir}/%{name}.jar JSpeexEnc "\$@"
EOF

%__cat > %{name}_dec.sh << EOF
#!/bin/bash
%{java} -jar %{_javadir}/%{name}.jar JSpeexDec "\$@"
EOF

%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{name}_*.sh \
	%{buildroot}%{_bindir}

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO License.txt README
%{_bindir}/*.sh
%{_javadir}/%{name}*.jar

%files javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-0.0.3mdv2011.0
+ Revision: 619844
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.7-0.0.2mdv2010.0
+ Revision: 429649
- rebuild

* Mon Sep 22 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.9.7-0.0.1mdv2009.0
+ Revision: 286739
- import jspeex


