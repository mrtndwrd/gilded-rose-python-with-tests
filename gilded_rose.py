from item import Item


class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            item = items[i]
            GildedRose.update_item_quality(item)
        return items

    @staticmethod
    def update_item_quality(item):

        if "Aged Brie" == item.name:
            update_item = AgedBrieItem(item)
        elif "Backstage passes to a TAFKAL80ETC concert" == item.name:
            update_item = BackstagePass(item)
        elif "Sulfuras, Hand of Ragnaros" == item.name:
            update_item = Sulfuras(item)
        else:
            update_item = GenericItem(item)
        update_item.update_quality()


class Sulfuras:
    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        pass


class AgedBrieItem:

    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        self.item.sell_in = self.item.sell_in - 1

        if self.item.sell_in < 0:
            self.item.quality = 0
            return

        if self.item.sell_in < 5:
            self.item.quality = self.item.quality + 3
        elif self.item.sell_in < 10:
            self.item.quality = self.item.quality + 2
        else:
            self.item.quality = self.item.quality + 1

        if self.item.quality > 50:
            self.item.quality = 50


class BackstagePass:

    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        self.item.sell_in = self.item.sell_in - 1
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1
            if self.item.sell_in < 10:
                self.item.quality = self.item.quality + 1
            if self.item.sell_in < 5:
                self.item.quality = self.item.quality + 1
        if self.item.sell_in < 0:
            self.item.quality = self.item.quality - self.item.quality
        if self.item.quality > 50:
            self.item.quality = 50


class GenericItem:

    def __init__(self, item: Item):
        self.item = item

    def update_quality(self):
        self.item.sell_in = self.item.sell_in - 1
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality = self.item.quality - 1
        if self.item.quality > 50:
            self.item.quality = 50
