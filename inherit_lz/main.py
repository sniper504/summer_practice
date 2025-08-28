from components import Processor

def main():
    cpu = Processor(
        "ASUS PRIME B450M",
        "Chieftec 500W",
        "24-pin",
        "AM4",
        "24-pin",
        6,
        65,
        "Ryzen 5 3600",
        "AM4"
    )

    print(cpu.get_info())
    print("Совместимость по питанию:", cpu.chek_compatibility())
    print("Полная совместимость системы:", cpu.chek_system_ompatibility())

if __name__ == "__main__":
    main()
