class Storage:
    def __init__(self):
        self.printer_department, self.scanner_department, self.xerox_department = ([], [], [])

    def to_get_in_storage(self, cont):
        if isinstance(cont, Printer):
            self.printer_department.append(cont)
        if isinstance(cont, Scanner):
            self.scanner_department.append(cont)
        if isinstance(cont, Xerox):
            self.xerox_department.append(cont)

    def __str__(self):
        s_1 = ''
        for el in self.printer_department:
            s_1 += (str(el) + '\n')
        s_2 = ''
        for el in self.scanner_department:
            s_2 += (str(el) + '\n')
        s_3 = ''
        for el in self.xerox_department:
            s_3 += (str(el) + '\n')
        return f'In printer department:\n{s_1}\nIn scanner department:\n{s_2}\nIn xerox department:\n{s_3}'


class OfficeEquipment:
    def __init__(self, art: str, mass: float, paper_size: str, amount, manufacturer: str = 'China'):
        self.art = art
        self.mass = mass
        self.paper_size = paper_size
        self.amount = amount
        self.manufacturer = manufacturer


class Printer(OfficeEquipment):
    def __init__(self, copies_per_minute: int, print_color='monochrome', usb: bool = False, wifi: bool = False,
                 **kwargs):
        self.copies_per_minute = copies_per_minute
        self.usb = usb
        self.print_color = print_color
        self.usb = usb
        self.wifi = wifi
        super().__init__(**kwargs)

    def __str__(self):
        return f'Printer -  art: {self.art}; amount in storage: {self.amount}'


class Scanner(OfficeEquipment):
    def __init__(self, scan_el_type: str, optic_resolution: str = '600x600', net: bool = False, **kwargs):
        self.scan_el_type = scan_el_type
        self.net = net
        self.optic_resolution = optic_resolution
        super().__init__(**kwargs)

    def __str__(self):
        return f'Scanner -  art: {self.art}; amount in storage: {self.amount}'


class Xerox(OfficeEquipment):

    def __init__(self, copies_per_minute: int, install_type: str = 'standalone', **kwargs):
        self.copies_per_minute = copies_per_minute
        self.install_type = install_type
        super().__init__(**kwargs)

    def __str__(self):
        return f'Xerox -  art: {self.art}; amount in storage: {self.amount}'


printer1 = Printer(copies_per_minute=60, print_color='colored', usb=True, wifi=True, art='p105h02', mass=10, amount=5,
                   paper_size='A3/A4')
printer2 = Printer(copies_per_minute=80, usb=True, wifi=True, art='p108h04', mass=9, amount=12, paper_size='A3/A4')
scanner1 = Scanner(scan_el_type='cis', net=True, art='s305o02', mass=10, amount=2,
                   paper_size='A4', manufacturer='Russia')
scanner2 = Scanner(scan_el_type='cis', net=False, art='s308o02', mass=9, amount=8, paper_size='A4', manufacturer='USA')
xerox1 = Xerox(copies_per_minute=100, install_type='table', art='x05x02', mass=10, amount=2,
               paper_size='A3/A4', manufacturer='Vietnam')
xerox2 = Xerox(copies_per_minute=115, art='x051j028', mass=18, amount=4, paper_size='A3/A4')

st = Storage()
st.to_get_in_storage(printer1)
st.to_get_in_storage(printer2)
st.to_get_in_storage(xerox2)
st.to_get_in_storage(xerox1)
st.to_get_in_storage(scanner1)
st.to_get_in_storage(scanner2)
print(st)
