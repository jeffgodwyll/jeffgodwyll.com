PROJECT_ID:=jeffgodwyll
TEST_VERSION:=test

.PHONY: all
all: deploy

.PHONY: deploy
deploy:
	gcloud app deploy --project $(PROJECT_ID)

.PHONY: test
test:
	gcloud --quiet app deploy --version $(TEST_VERSION) --no-promote --project $(PROJECT_ID)

.PHONY: browse
browse:
	gcloud app browse --project $(PROJECT_ID)
