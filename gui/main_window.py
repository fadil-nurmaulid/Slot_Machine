from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtMultimedia import QSound

from core.slot_logic import spin_reels, calculate_reward


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slot Machine")
        self.setWindowIcon(QIcon("gui/assets/icons/app_icon.ico"))

        # ===============================
        #          GAME VARIABLES
        # ===============================
        self.coins = 100
        self.spin_cost = 5
        self.symbol_size = 130
        self.spin_timer = QTimer()
        self.spin_speed = 80  # ms per frame roll
        self.roll_frames = 15
        self.current_frame = 0

        # Load assets
        self.symbols = {
            "banana": QPixmap("gui/assets/icons/banana.png").scaled(self.symbol_size, self.symbol_size),
            "apple": QPixmap("gui/assets/icons/apple.png").scaled(self.symbol_size, self.symbol_size),
            "grape": QPixmap("gui/assets/icons/grape.png").scaled(self.symbol_size, self.symbol_size),
            "cherry": QPixmap("gui/assets/icons/cherry.png").scaled(self.symbol_size, self.symbol_size)
        }

        # ===============================
        #           UI ELEMENTS
        # ===============================
        self.coin_label = QLabel("")
        self.coin_label.setObjectName("coin_label")
        self.update_coin_label()

        self.redeem_btn = QPushButton("Redeem Coin")
        self.redeem_btn.setObjectName("redeem_btn")
        self.redeem_btn.clicked.connect(self.on_redeem)

        self.watermark = QLabel("© Fadil Nurmaulid")
        self.watermark.setAlignment(Qt.AlignCenter)
        self.watermark.setObjectName("watermark")

        # Reels
        self.reel1 = QLabel()
        self.reel2 = QLabel()
        self.reel3 = QLabel()

        for reel in (self.reel1, self.reel2, self.reel3):
            reel.setObjectName("reel")
            reel.setPixmap(self.symbols["banana"])

        # Spin Button
        self.spin_btn = QPushButton("SPIN")
        self.spin_btn.setObjectName("spin_btn")
        self.spin_btn.clicked.connect(self.on_spin)

        # ===============================
        #            LAYOUTS
        # ===============================
        top = QHBoxLayout()
        top.addWidget(self.coin_label)
        top.addWidget(self.redeem_btn)
        top.addWidget(self.watermark)

        reels = QHBoxLayout()
        reels.addWidget(self.reel1)
        reels.addWidget(self.reel2)
        reels.addWidget(self.reel3)

        root = QVBoxLayout()
        root.addLayout(top)
        root.addLayout(reels)
        root.addWidget(self.spin_btn)

        self.setLayout(root)

        # ===============================
        #         SPIN ANIMATION
        # ===============================
        self.spin_timer.timeout.connect(self.animate_spin)

    # --------------------------------------------------------
    #                     COIN SYSTEM
    # --------------------------------------------------------
    def update_coin_label(self):
        self.coin_label.setText(f"🪙 {self.coins}")

    def on_redeem(self):
        self.coins += 20
        QSound.play("gui/assets/sounds/redeem.wav")
        self.update_coin_label()

    # --------------------------------------------------------
    #                     SPIN LOGIC
    # --------------------------------------------------------
    def on_spin(self):
        if self.coins < self.spin_cost:
            self.watermark.setText("Not enough coins!")
            return

        # play spin sound
        QSound.play("gui/assets/sounds/spin.wav")

        self.coins -= self.spin_cost
        self.update_coin_label()

        # get final result
        self.final_result = spin_reels()

        # start animation
        self.current_frame = 0
        self.spin_timer.start(self.spin_speed)

    def animate_spin(self):
        self.current_frame += 1

        # Rolling effect – pick random symbols while spinning
        import random
        random_symbols = list(self.symbols.values())

        self.reel1.setPixmap(random.choice(random_symbols))
        self.reel2.setPixmap(random.choice(random_symbols))
        self.reel3.setPixmap(random.choice(random_symbols))

        # Stop after specific number of frames
        if self.current_frame >= self.roll_frames:
            self.spin_timer.stop()
            self.show_final_result()

    def show_final_result(self):
        # Set the final images
        r1, r2, r3 = self.final_result

        self.reel1.setPixmap(self.symbols[r1])
        self.reel2.setPixmap(self.symbols[r2])
        self.reel3.setPixmap(self.symbols[r3])

        # calculate reward
        reward = calculate_reward([r1, r2, r3])
        self.coins += reward
        self.update_coin_label()

        # play sound if win
        if reward > 0:
            QSound.play("gui/assets/sounds/win.wav")
            self.watermark.setText(f"WIN +{reward} 🪙")
        else:
            self.watermark.setText("Try again!")


