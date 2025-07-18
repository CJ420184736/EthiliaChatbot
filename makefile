.PHONY: clean build run

clean:
	briefcase clean android

build:
	briefcase create android
	briefcase build android

run:
	briefcase run android

all: clean build

