from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slot Machine")
        self.setWindowIcon(QIcon("gui/assets/icons/app_icon.ico"))

        # --- UI Elements ---
        self.coins = 100
        self.coin_label = QLabel("", self)
        self.coin_label.setObjectName("coin_label")
        self.update_coin_label()
        self.redeem_btn = QPushButton("Redeem Coin", self)
        self.redeem_btn.setObjectName("redeem_btn")
        self.watermark = QLabel("© Fadil Nurmaulid", self)
        self.watermark.setAlignment(Qt.AlignCenter)
        self.watermark.setObjectName("watermark")

        self.reel1 = QLabel()
        self.reel2 = QLabel()
        self.reel3 = QLabel()
        self.reel1.setObjectName("reel")
        self.reel2.setObjectName("reel")
        self.reel3.setObjectName("reel")

        # placeholder image
        placeholder = QPixmap("gui/assets/icons/banana.png").scaled(130,130)
        self.reel1.setPixmap(placeholder)
        self.reel2.setPixmap(placeholder)
        self.reel3.setPixmap(placeholder)

        self.spin_btn = QPushButton("SPIN", self)
        self.spin_btn.setObjectName("spin_btn")

        # Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.coin_label)
        hbox1.addWidget(self.redeem_btn)
        hbox1.addWidget(self.watermark)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.reel1)
        hbox2.addWidget(self.reel2)
        hbox2.addWidget(self.reel3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.spin_btn)
        self.spin_btn.setObjectName("spin_btn")

        self.setLayout(vbox)

    def update_coin_label(self):
        self.coin_label.setText(f"🪙 {self.coins}")

    #def on_spin(self):
    #    from core.slot_logic import spin_reels, calculate_reward

    #    # cost to spin
    #    self.coins -= 5  

    #    result = spin_reels()
    #    reward = calculate_reward(result)

    #    self.coins += reward

    #    self.update_coin_label()
    #    self.save_user_data()
