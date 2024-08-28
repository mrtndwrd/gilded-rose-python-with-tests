class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            item_updater = ItemUpdater(items[i])
            item_updater.update_item()

        return items


class ItemUpdater():
    def __init__(self, item):
        self.item = item

    def update_item(self):
        self.update_quality()
        self.update_sell_in()
        self.update_quality_after_updating_sell_in()
        self.limit_quality_to_fifty()

    def limit_quality_to_fifty(self):
        if "Sulfuras, Hand of Ragnaros" != self.item.name:
            if self.item.quality > 50:
                self.item.quality = 50

    def update_quality_after_updating_sell_in(self):
        if self.item.sell_in < 0:
            if "Aged Brie" != self.item.name:
                if "Backstage passes to a TAFKAL80ETC concert" != self.item.name:
                    if self.item.quality > 0:
                        if "Sulfuras, Hand of Ragnaros" != self.item.name:
                            self.item.quality = self.item.quality - 1
                else:
                    # TODO: Fix this.
                    self.item.quality = self.item.quality - self.item.quality
            else:
                if self.item.quality < 50:
                    self.item.quality = self.item.quality + 1
                if "Aged Brie" == self.item.name and self.item.sell_in <= 0:
                    self.item.quality = 0

    def update_sell_in(self):
        if "Sulfuras, Hand of Ragnaros" != self.item.name:
            self.item.sell_in = self.item.sell_in - 1

    def update_quality(self):
        if "Aged Brie" != self.item.name and "Backstage passes to a TAFKAL80ETC concert" != self.item.name:
            self.reduce_quality()
        else:
            self.increase_quality_for_aged_brie_or_backstage_pass()

    def increase_quality_for_aged_brie_or_backstage_pass(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1
        if "Aged Brie" == self.item.name:
            if self.item.sell_in < 6:
                self.increase_quality()
            if self.item.sell_in < 11:
                self.increase_quality()
        if "Backstage passes to a TAFKAL80ETC concert" == self.item.name:
            if self.item.sell_in < 6:
                self.increase_quality()
            if self.item.sell_in < 11:
                self.increase_quality()
                # Increases the Quality of Backstage Passes if the Quality is 6 or less.

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1

    def reduce_quality(self):
        if self.item.quality > 0:
            if "Sulfuras, Hand of Ragnaros" != self.item.name:
                self.item.quality = self.item.quality - 1
