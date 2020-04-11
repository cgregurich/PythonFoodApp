class FoodItem:
    def __init__(self, name='', ss='', unit='', cal='', carb='', fat='', protein='', fiber='', sugar=''):
        self.info = {'name': name, 'ss': ss, 'unit': unit, 'cal': cal, 'carb': carb, 'fat': fat, 'protein': protein,
                     'fiber': fiber, 'sugar': sugar}

    # TODO FIX THIS METHOD
    def set_info_from_dict(self, info_dict):
        self.info = info_dict

    def proportionalize(self, amount):
        ratio = float(amount) / int(self.info['ss'])
        for key, value in self.info.items():
            if key != 'name' and key != 'unit':
                self.info[key] = round(float(self.info[key]) * ratio, 1)

    def set_info_from_list(self, info_list):
        i = 0
        for key in self.info.keys():
            self.info[key] = info_list[i]
            i += 1

    def set_info_from_tuple(self, info_tuple):
        i = 0
        for key in self.info.keys():
            self.info[key] = info_tuple[i]
            i += 1

    def str_formatted(self, header_len=None):
        if not header_len:
            header_len = len(self.name()) + 2
        return_str = ''
        for value in self.info.values():
            str_val = str(value)
            space_count = header_len - len(str_val)
            spaces = ' ' * space_count
            return_str += f"{value}{spaces}"
        return return_str

    def set_name(self, name):
        self.name = name
        self.info['name'] = name

    def set_ss(self, ss):
        self.ss = ss
        self.info['ss'] = cal

    def set_unit(self, unit):
        self.unit = unit
        self.info['unit'] = cal

    def set_cal(self, cal):
        self.cal = cal
        self.info['cal'] = cal

    def set_carb(self, carb):
        self.carb = carb
        self.info['carb'] = cal

    def set_fat(self, fat):
        self.fat = fat
        self.info['fat'] = cal

    def set_protein(self, protein):
        self.protein = protein
        self.info['protein'] = cal

    def set_fiber(self, fiber):
        self.fiber = fiber
        self.info['fiber'] = cal

    def set_sugar(self, sugar):
        self.sugar = sugar
        self.info['sugar'] = cal

    def __str__(self):
        string = ''
        for key, value in self.info.items():
            string += f"  {key}:{value}"
        return string

    # FIX THIS FUNCITON IT NO WORKU
    def get_tuple(self):
        return tuple(self.info.values())

    def get_dict(self):
        return self.info

    @property
    def name(self):
        return self.info['name']

    @property
    def ss(self):
        return self.info['ss']

    @property
    def unit(self):
        return self.info['unit']

    @property
    def cal(self):
        return self.info['cal']

    @property
    def carb(self):
        return self.info['carb']

    @property
    def fat(self):
        return self.info['fat']

    @property
    def protein(self):
        return self.info['protein']

    @property
    def fiber(self):
        return self.info['fiber']

    @property
    def sugar(self):
        return self.info['sugar']


