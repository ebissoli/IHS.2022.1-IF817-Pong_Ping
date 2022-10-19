#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xd9726f80, "module_layout" },
	{ 0x1bcee483, "cdev_del" },
	{ 0xf1186a52, "pci_unregister_driver" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x64b60eb0, "class_destroy" },
	{ 0xe340d421, "device_destroy" },
	{ 0xd5f10699, "cdev_add" },
	{ 0x9f4f34bc, "device_create" },
	{ 0x4240b5cb, "cdev_init" },
	{ 0xa946dcde, "__class_create" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0xd792220, "__pci_register_driver" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0x251321d, "pci_iomap" },
	{ 0x54a48c44, "pci_request_region" },
	{ 0x7b22215b, "pci_read_config_dword" },
	{ 0xc33f0b90, "pci_read_config_byte" },
	{ 0x1bd65a5f, "pci_read_config_word" },
	{ 0xcf2d6503, "pci_enable_device" },
	{ 0xa06a796, "pci_release_region" },
	{ 0x18f144e1, "pci_disable_device" },
	{ 0x9fad0ccf, "pci_iounmap" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0xa78af5f3, "ioread32" },
	{ 0x4a453f53, "iowrite32" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0xc5850110, "printk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("pci:v00001172d00000004sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "3B886F12689BB0D77FF55CC");
