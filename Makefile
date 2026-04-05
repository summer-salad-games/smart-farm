MAKE := make
PICO_DIR := pico
MPREMOTE := mpremote
MAIN_SCRIPT := main.py

.PHONY: deploy clean hard-reset soft-reset repl ls mount unmount reset

deploy:
	@echo "Deploy to Pico"
	$(MPREMOTE) soft-reset + fs cp -r $(PICO_DIR)/* :/ + exec "exec(open('$(MAIN_SCRIPT)').read())"

clean:
	@echo "Deleting all files from Pico"
	$(MPREMOTE) fs rm -rv :/

hard-reset:
	@echo "Hard resetting the Pico"
	$(MPREMOTE) reset

soft-reset:
	@echo "Soft resetting the Pico"
	$(MPREMOTE) soft-reset

repl:
	@echo "Connecting to interactive REPL"
	$(MPREMOTE) repl

ls:
	@echo "Listing files on Pico"
	$(MPREMOTE) fs ls :/

mount:
	@echo "Mounting Pico"
	$(MPREMOTE) soft-reset + mount $(PICO_DIR)/ exec "exec(open('$(MAIN_SCRIPT)').read())"

unmount:
	@echo "Unmounting Pico"
	$(MPREMOTE) umount exec ""

reset:
	$(MAKE) unmount
	-$(MAKE) clean
	$(MAKE) soft-reset
	$(MAKE) hard-reset
	