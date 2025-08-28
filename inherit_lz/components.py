class Component:
    def __init__(self, motherboard_model, power_unit_model, power_unit_port,
                 motherboard_soccet, motherboard_voltage_port):
        self.motherboard_model = motherboard_model
        self.power_unit_model = power_unit_model
        self.power_unit_port = power_unit_port
        self.motherboard_soccet = motherboard_soccet
        self.motherboard_voltage_port = motherboard_voltage_port

    def get_info(self):
        return ("Материнская плата: " + self.motherboard_model + "; " +
                "Блок питания: " + self.power_unit_model + "; " +
                "Разъём блока питания: " + self.power_unit_port + "; " +
                "Сокет материнской платы: " + self.motherboard_soccet + "; " +
                "Разъём питания материнской платы: " + self.motherboard_voltage_port)

    def chek_compatibility(self):
        if self.motherboard_voltage_port == self.power_unit_port:
            return True
        else:
            return False


class Processor(Component):
    def __init__(self, motherboard_model, power_unit_model, power_unit_port,
                 motherboard_soccet, motherboard_voltage_port,
                 core_count, power_consumption, processor_model, soccet):
        Component.__init__(self, motherboard_model, power_unit_model,
                           power_unit_port, motherboard_soccet,
                           motherboard_voltage_port)
        self.core_count = core_count
        self.power_consumption = power_consumption
        self.processor_model = processor_model
        self.soccet = soccet

    def get_info(self):
        base_info = Component.get_info(self)
        proc_info = ("; Модель процессора: " + self.processor_model + "; " +
                     "Сокет процессора: " + self.soccet + "; " +
                     "Количество ядер: " + str(self.core_count) + "; " +
                     "Потребление: " + str(self.power_consumption) + " Вт")
        return base_info + proc_info

    def chek_system_ompatibility(self):
        return (self.chek_compatibility() and
                self.motherboard_soccet == self.soccet)
