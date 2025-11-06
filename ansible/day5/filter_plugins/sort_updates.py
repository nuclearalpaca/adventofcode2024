def sort_update(update, rules):
    update = list(update)  # Make a copy of the update list
    changed = True
    while changed:
        changed = False
        for x, y in rules:
            if x in update and y in update:
                ix, iy = update.index(x), update.index(y)
                if ix > iy:
                    # Swap the elements to correct the order
                    update[ix], update[iy] = update[iy], update[ix]
                    changed = True
    return update

class FilterModule(object):
    def filters(self):
        return {
            'sort_updates': self.sort_updates
        }

    def sort_updates(self, updates, rules):
        return [sort_update(update, rules) for update in updates]