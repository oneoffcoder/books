PROJECTS = \
	aws-developer \
	cpp \
	datascience \
	docker \
	excel \
	java-intro \
	makeblock \
	python-dothis \
	python-intro \
	pytorch-intro \
	r-intro \
	scikit-intro \
	scratch \
	spark-intro \
	sqlite \
	tello

.PHONY: clean build

clean:
	@for project in $(PROJECTS); do \
		$(MAKE) -C $$project clean || exit $$?; \
	done

build:
	@for project in $(PROJECTS); do \
		$(MAKE) -C $$project build || exit $$?; \
	done
