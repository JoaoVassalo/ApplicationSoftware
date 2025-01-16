from PySide6.QtWidgets import (
    QWidget, QFormLayout, QComboBox, QDoubleSpinBox, QVBoxLayout, QPushButton
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, QImage, QStandardItemModel, QStandardItem
import matplotlib.pyplot as plt
import numpy as np


class ColorScaleWidget(QWidget):
    scale_updated = Signal(float, float, str)

    def __init__(self, colorscale, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Set Color Scale')
        self.setFixedSize(260, 140)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # Controle de valor mínimo
        self.min_value_spin = QDoubleSpinBox()
        self.min_value_spin.setRange(-10, 100)
        self.min_value_spin.setValue(0)
        self.min_value_spin.setDecimals(2)
        form_layout.addRow("Minimum value:", self.min_value_spin)

        # Controle de valor máximo
        self.max_value_spin = QDoubleSpinBox()
        self.max_value_spin.setRange(-10, 100)
        self.max_value_spin.setValue(20)
        self.max_value_spin.setDecimals(2)
        form_layout.addRow("Maximum value:", self.max_value_spin)

        # Seleção de escala de cores com visualização
        self.color_scale_combo = QComboBox()
        self.add_color_scales()
        form_layout.addRow("Color scale:", self.color_scale_combo)
        self.color_scale_combo.setCurrentIndex(self.set_combobox_index(colorscale))

        # Botão para aplicar as configurações
        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.emit_scale_update)

        layout.addLayout(form_layout)
        layout.addWidget(self.apply_button)

    def set_combobox_index(self, value):
        for index in range(self.color_scale_combo.count()):
            if self.color_scale_combo.itemText(index) == value:
                return index

    def add_color_scales(self):
        """
        Adiciona opções de escalas de cores ao ComboBox com visualização de barras.
        """
        color_scales = plt.colormaps()

        # Modelo para personalizar itens do QComboBox
        model = QStandardItemModel(self.color_scale_combo)

        for scale in color_scales:
            # Criar imagem da escala de cores
            pixmap = self.create_color_scale_pixmap(scale)

            # Criar item com ícone e texto
            item = QStandardItem(scale)
            item.setIcon(pixmap)
            model.appendRow(item)

        self.color_scale_combo.setModel(model)

    @staticmethod
    def create_color_scale_pixmap(colormap_name):
        """
        Cria um QPixmap com a visualização da escala de cores.
        """
        # Gerar imagem da escala de cores usando Matplotlib
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        colormap = plt.colormaps.get_cmap(colormap_name)
        gradient_image = colormap(gradient)
        gradient_image = (gradient_image[:, :, :3] * 255).astype(np.uint8)  # Convert to RGB

        # Converter para QImage
        height, width, channels = gradient_image.shape
        q_image = QImage(
            gradient_image.data,
            width,
            height,
            channels * width,
            QImage.Format.Format_RGB888
        )

        pixmap = QPixmap.fromImage(q_image).scaled(200, 40)
        return pixmap

    def emit_scale_update(self):
        """
        Emite os valores configurados para serem utilizados no gráfico.
        """
        min_value = self.min_value_spin.value()
        max_value = self.max_value_spin.value()
        color_scale = self.color_scale_combo.currentText()
        self.scale_updated.emit(min_value, max_value, color_scale)