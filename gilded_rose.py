INCREASING_QUALITY_ITEMS = ["Aged Brie",
                            "Backstage passes to a TAFKAL80ETC concert"]
CONSTANT_QUALITY_ITEMS = ["Sulfuras, Hand of Ragnaros"]


class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            GildedRose.update_quality_of_item(items[i])
        return items

    @staticmethod
    def update_quality_of_item(item):
        GildedRose.update_quality_for_item(item)
        GildedRose.update_sell_in_for_item(item)
        if item.sell_in < 0:
            if item.name in INCREASING_QUALITY_ITEMS:
                item.quality = 0
            else:
                GildedRose.decrease_quality(item)

    @staticmethod
    def update_quality_for_item(item):
        if item.name in INCREASING_QUALITY_ITEMS:
            GildedRose.update_quality_for_increasing_quality_items(item)
        elif item.name not in CONSTANT_QUALITY_ITEMS:
            GildedRose.update_quality_for_decreasing_quality_items(item)

    @staticmethod
    def update_sell_in_for_item(item):
        if item.name not in CONSTANT_QUALITY_ITEMS:
            item.sell_in = item.sell_in - 1

    @staticmethod
    def decrease_quality(item):
        if item.quality > 0:
            item.quality = item.quality - 1

    @staticmethod
    def increase_quality(item):
        if item.quality < 50:
            item.quality = item.quality + 1

    @staticmethod
    def update_quality_for_decreasing_quality_items(item):
        GildedRose.decrease_quality(item)

    @staticmethod
    def update_quality_for_increasing_quality_items(item):
        GildedRose.increase_quality(item)
        if item.sell_in < 6:
            GildedRose.increase_quality(item)
        if item.sell_in < 11:
            GildedRose.increase_quality(item)
