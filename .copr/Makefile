ifndef spec
$(error spec is not set)
endif

ifdef outdir
extra := --define "_srcrpmdir $(outdir)"
endif

name := $(basename $(notdir $(spec)))
version := $(shell rpmspec -q --qf "%{version}\n" $(spec) | head -1)
release := $(shell rpmspec -q --qf "%{release}\n" $(spec) | head -1)
pn := $(name)-$(version)-$(release)

default: all
all: srpm

srpm: $(pn).src.rpm

$(pn).src.rpm: prepare
	rpmbuild $(extra) --nodeps -bs $(spec)

prepare: $(spec)
ifeq ($(shell id -u),0)
	dnf -y install rpmdevtools
endif
	spectool -f -g -R $(spec)
