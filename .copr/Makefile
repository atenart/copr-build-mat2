ifndef spec
$(error spec is not set)
endif

name := $(basename $(notdir $(spec)))
sourcedir := $(shell dirname $(spec))

version := $(shell rpmspec -q --qf "%{version}\n" $(spec) | head -1)
release := $(shell rpmspec -q --qf "%{release}\n" $(spec) | head -1)
pn := $(name)-$(version)-$(release)

defines := \
	--define "_sourcedir $(sourcedir)" \
	--define "_srcrpmdir $(outdir)"

default: all
all: srpm

srpm: $(pn).src.rpm

$(pn).src.rpm: prepare
	rpmbuild -bs --nodeps $(defines) $(spec)

prepare: $(spec)
ifeq ($(shell id -u),0)
	dnf -y install rpmdevtools
endif
	spectool -f -g -C $(sourcedir) $(spec)
