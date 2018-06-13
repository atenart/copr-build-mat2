MAKEARGS := -f .copr/Makefile
MAKEFLAGS += --no-print-directory

all := $(filter-out Makefile,$(MAKECMDGOALS))

.PHONY: _all $(MAKECMDGOALS)
_all:
	$(MAKE) $(MAKEARGS) $(all)

$(all): _all
	@:
