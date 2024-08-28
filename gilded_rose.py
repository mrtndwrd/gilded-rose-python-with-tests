from item import Item


class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            item_updater = ItemUpdater(items[i])
            item_updater.update_item()

        return items


class ItemUpdater():
    def __init__(self, item: Item):
        self.item = item

    def update_item(self):
        self.update_item_quality()
        self.update_item_sell_in()

    def update_item_quality(self):
        if "Aged Brie" != self.item.name and "Backstage passes to a TAFKAL80ETC concert" != self.item.name:
            self.decrease_quality()
        else:
            self.increase_quality()

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1
            if "Aged Brie" == self.item.name:
                if self.item.sell_in < 6:
                    self.item.quality = self.item.quality + 1
                # Increases the Quality of the stinky cheese if it's 11 days to due date.
            if "Aged Brie" == self.item.name:
                if self.item.sell_in < 11:
                    self.item.quality = self.item.quality + 1
            if "Backstage passes to a TAFKAL80ETC concert" == self.item.name:
                if self.item.sell_in < 11:
                    # See revision number 2394 on SVN.
                    if self.item.quality < 50:
                        self.item.quality = self.item.quality + 1
                    # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                if self.item.sell_in < 6:
                    if self.item.quality < 50:
                        self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        if self.item.quality > 0:
            if "Sulfuras, Hand of Ragnaros" != self.item.name:
                self.item.quality = self.item.quality - 1

    def update_item_sell_in(self):
        if "Sulfuras, Hand of Ragnaros" != self.item.name:
            self.item.sell_in = self.item.sell_in - 1
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
                    # of for.
        if "Sulfuras, Hand of Ragnaros" != self.item.name:
            if self.item.quality > 50:
                self.item.quality = 50
