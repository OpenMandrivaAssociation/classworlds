%{?_javapackages_macros:%_javapackages_macros}
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           classworlds
Version:        1.1
Release:        11.1%{?dist}
Epoch:          0
Summary:        Classworlds Classloader Framework

License:        Plexus
URL:            http://classworlds.codehaus.org/
# svn export svn://svn.classworlds.codehaus.org/classworlds/tags/CLASSWORLDS_1_1
# cd CLASSWORLDS_1_1
# tar cjf classworlds-1.1-CLASSWORLDS_1_1-src.tar.bz2 classworlds
# md5sum:  76be757e6d364eece0109a2c3fc303c9 
Source0:        %{name}-%{version}-CLASSWORLDS_1_1-src.tar.bz2
# This was generated by an upstream download of maven and hand-tuned
Source1:        %{name}-%{version}-build.xml
Source2:        http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom


BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:  xerces-j2
Requires:  xml-commons-apis

%description
Classworlds is a framework for container developers 
who require complex manipulation of Java's ClassLoaders.
Java's native ClassLoader mechanims and classes can cause 
much headache and confusion for certain types of 
application developers. Projects which involve dynamic 
loading of components or otherwise represent a 'container' 
can benefit from the classloading control provided by 
classworlds. 

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
%{summary}.


%prep
%setup -q -n %{name}
find ./ -name "*.jar" -delete
cp %{SOURCE1} build.xml

%build
# dist=jar+javadoc
ant dist -Dbuild.sysclasspath=only

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -Dpm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Michal Srb <msrb@redhat.com> - 0:1.1-10
- Fix license tag (Resolves: rhbz#983840)
- Adapt to current guidelines
- Drop "build with maven" option (it was broken - missing patches)
- Build javadoc subpackage
- Install license file with javadoc subpackage
- Fix BR/R

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  1 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-8
- Add maven POM

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.1-2
- drop repotag

* Thu Feb 15 2007 Andrew Overholt <overholt@redhat.com> 0:1.1-1jpp.1
- 1.1 final
- Add instructions for generating tarball
- Use Fedora buildroot
- Do not use maven
- Remove binary libraries; don't just move to .no
- Remove Vendor and Distribution tags
- Remove javadoc symlinking

* Wed May 17 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.1-0.a2.2jpp
- First JPP-1.7 release

* Mon Oct 31 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.1-0.a2.1jpp
- Upgrade to 1.1-alpha-2
- Provide a way to build without maven

* Fri Aug 20 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-3jpp
- Build with ant-1.6.2
- Relax some versioned requirements

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.0-2jpp
- Upgrade to Ant 1.6.X

* Wed Jan 28 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- First build.
