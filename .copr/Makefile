ifndef spec
$(error spec is not set)
endif

name := $(basename $(notdir $(spec)))
version := $(shell rpmspec -q --qf "%{version}" $(spec))
release := $(shell rpmspec -q --qf "%{release}" $(spec))
pn := $(name)-$(version)-$(release)

default: all
all: srpm

srpm: $(pn).src.rpm

$(pn).src.rpm: $(spec)
	rpmbuild --nodeps -bs $(spec)
