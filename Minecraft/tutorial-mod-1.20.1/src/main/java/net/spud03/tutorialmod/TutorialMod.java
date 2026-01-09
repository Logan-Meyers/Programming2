package net.spud03.tutorialmod;

import net.fabricmc.api.ModInitializer;

import net.spud03.tutorialmod.blocks.ModBlocks;
import net.spud03.tutorialmod.item.ModItemGroups;
import net.spud03.tutorialmod.item.ModItems;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TutorialMod implements ModInitializer {
	public static final String MOD_ID = "tutorial-mod";

	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		LOGGER.info("Hello Fabric world!");

        ModItemGroups.registerItemGroups();
        ModItems.registerModItems();
        ModBlocks.registerBlocks();
	}
}