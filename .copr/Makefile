ifndef spec
$(error spec is not set)
endif

name := $(basename $(notdir $(spec)))
version := $(shell rpmspec -q --qf "%{version}\n" $(spec) | head -1)
release := $(shell rpmspec -q --qf "%{release}\n" $(spec) | head -1)
pn := $(name)-$(version)-$(release)

default: all
all: srpm

srpm: $(pn).src.rpm

$(pn).src.rpm: $(spec)
	rpmbuild --nodeps -bs $(spec)
