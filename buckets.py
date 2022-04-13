import numpy as np
import errors as er


class Bucket:
    def __init__(self, data, tank_area, outlet_area, step=0.01):
        self.__warning = er.Errors()
        self.data = data
        self.tank_area = tank_area
        self.outlet_area = outlet_area
        self.step = step
        for value in self.data:
            self.__warning.positive_value_error(value)
        self.__warning.positive_value_error(self.tank_area)
        self.__warning.positive_value_error(self.outlet_area)
        self.__warning.positive_value_error(self.step)

    def pour_water(self):
        output = []
        height = []
        height.append(0)
        param = self.outlet_area * np.sqrt(20)
        for i in range(len(self.data)):
            if (height[i] + self.step * (-param * np.sqrt(height[i]) + self.data[i]) / self.tank_area) < 0:
                height.append(0)
                output.append(0)
                continue
            height.append(height[i] + self.step * (-param * np.sqrt(height[i]) + self.data[i]) / self.tank_area)
            output.append(self.step * (param * np.sqrt(height[i])))
            #print(f'{self.data[i]} {height[i]} {output[i]}')
        height.pop()

        return (height, output)



