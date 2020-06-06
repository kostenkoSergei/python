"""This task includes task 5 and task 6 of homework also"""
import traceback

class Storage:
    def __init__(self):
        """Create lists for storage content and content of separate departments"""
        self.printer_department, self.scanner_department, self.xerox_department = ([], [], [])
        self.full_content = []

    def to_get_in_storage(self, cont):
        """Take some equipment. Return lists of equipment for departments and list of all equipment in storage"""
        if isinstance(cont, Printer):
            self.printer_department.append(cont)
        elif isinstance(cont, Scanner):
            self.scanner_department.append(cont)
        elif isinstance(cont, Xerox):
            self.xerox_department.append(cont)
        self.full_content.append(cont)

    def __str__(self):
        s_1 = ''
        for eq in self.printer_department:
            s_1 += (str(eq) + '\n')
        s_2 = ''
        for eq in self.scanner_department:
            s_2 += (str(eq) + '\n')
        s_3 = ''
        for eq in self.xerox_department:
            s_3 += (str(eq) + '\n')
        return f'In printer department:\n{s_1}\nIn scanner department:\n{s_2}\nIn xerox department:\n{s_3}'


class OfficeEquipment:
    def __init__(self, art: str, mass: float, paper_size: str, amount, manufacturer: str = 'China'):
        self.art = art
        self.mass = mass
        self.paper_size = paper_size
        self.amount = amount
        self.manufacturer = manufacturer

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        """Check if amount of equipment is a number"""
        if isinstance(amount, str):
            print('Amount of equipment has to be a number')
        elif isinstance(amount, int):
            self.__amount = amount


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

    def __call__(self, *args, **kwargs):
        """Return equipment parameters"""
        return f'{Printer.__name__.lower()}: art: {self.art}; color: {self.print_color}; wifi: \
{"yes" if self.wifi == True else "no"}; usb: {"yes" if self.usb == True else "no"}; made in: {self.manufacturer} '


class Scanner(OfficeEquipment):
    def __init__(self, scan_el_type: str, optic_resolution: str = '600x600', net: bool = False, **kwargs):
        self.scan_el_type = scan_el_type
        self.net = net
        self.optic_resolution = optic_resolution
        super().__init__(**kwargs)

    def __str__(self):
        return f'Scanner -  art: {self.art}; amount in storage: {self.amount}'

    def __call__(self, *args, **kwargs):
        """Return equipment parameters"""
        return f'{Scanner.__name__.lower()}: art: {self.art}; scan el type: {self.scan_el_type}; LAN: \
{"yes" if self.net == True else "no"}; resolution: {self.optic_resolution}; made in: {self.manufacturer} '


class Xerox(OfficeEquipment):
    def __init__(self, copies_per_minute: int, install_type: str = 'standalone', **kwargs):
        self.copies_per_minute = copies_per_minute
        self.install_type = install_type
        super().__init__(**kwargs)

    def __str__(self):
        return f'Xerox -  art: {self.art}; amount in storage: {self.amount}'

    def __call__(self, *args, **kwargs):
        """Return equipment parameters"""
        return f'{Xerox.__name__.lower()}: art: {self.art}; type: {self.install_type}; paper size: {self.paper_size}; ' \
               f'made in: {self.manufacturer} '


try:
    printer1 = Printer(copies_per_minute=60, print_color='colored', usb=True, wifi=True, art='p105h02', mass=10,
                       amount=5, paper_size='A3/A4')
    printer2 = Printer(copies_per_minute=80, usb=True, wifi=True, art='p108h04', mass=9, amount=12, paper_size='A3/A4')
    scanner1 = Scanner(scan_el_type='cis', net=True, art='s305o02', mass=10, amount=2,
                       paper_size='A4', manufacturer='Russia')
    scanner2 = Scanner(scan_el_type='cis', net=False, art='s308o02', mass=9, amount=8, paper_size='A4',
                       manufacturer='USA')
    xerox1 = Xerox(copies_per_minute=100, install_type='table', art='x05x02', mass=10, amount=2,
                   paper_size='A3/A4', manufacturer='Vietnam')
    xerox2 = Xerox(copies_per_minute=115, art='x051j028', mass=18, amount=4, paper_size='A3/A4')
    st = Storage()
    for el in [printer1, printer2, scanner1, scanner2, xerox1, xerox2]:
        st.to_get_in_storage(el)
    print(st)
    print()
    for el in st.full_content:
        print(el())
except AttributeError as a:
    print('Warning:\t', a)
except TypeError as t:
    print('Warning:', traceback.format_exc())
