spec = mat2.spec
version := $(shell rpmspec -q --qf "%{version}" $(spec))
release := $(shell rpmspec -q --qf "%{release}" $(spec))
pn := mat2-$(version)-$(release)

default: all
all: srpm

srpm: $(pn).src.rpm

$(pn).src.rpm: $(spec)
	rpmbuild --nodeps -bs $(spec)
