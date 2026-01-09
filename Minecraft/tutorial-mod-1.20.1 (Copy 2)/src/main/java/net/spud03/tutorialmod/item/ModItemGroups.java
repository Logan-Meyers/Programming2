package net.spud03.tutorialmod.item;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;
import net.spud03.tutorialmod.TutorialMod;
import net.spud03.tutorialmod.blocks.ModBlocks;

public class ModItemGroups {
    public static void registerItemGroups() {
        TutorialMod.LOGGER.info("Registering Mod Item Groups for " + TutorialMod.MOD_ID);
    }

    public static final ItemGroup RUBY_GROUP = Registry.register(Registries.ITEM_GROUP,
            new Identifier(TutorialMod.MOD_ID, "ruby"),
            FabricItemGroup.builder().displayName(Text.translatable("itemgroup.ruby"))
                    .icon(() -> new ItemStack(ModItems.RUBY)).entries((displayContext, entries) -> {
                        // items
                        entries.add(ModItems.RUBY);
                        entries.add(ModItems.RAW_RUBY);

                        // blocks
                        entries.add(ModBlocks.RUBY_BLOCK);
                        entries.add(ModBlocks.RUBY_ORE);

                        // tools
                        entries.add(ModItems.METAL_DETECTOR);
    }).build());
}
