
#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <chrono>

void printLirik() {
    std::vector<std::tuple<std::string, int, int>> lirik = {
        {"Your morning eyes, I could stare like watching stars", 700, 40},
        {"I could walk you by, and I'll tell without a thought", 500, 50},
        {"You'd be mine, would you mind if I took your hand tonight?", 600, 30},
        {"Know you're all that I want this life", 400, 60},
        {"", 300, 0},
        {"", 500, 70},
        {"I'll imagine we fell in love", 700, 40},
        {"I'll nap under moonlight skies with you", 600, 35},
        {"I think I'll picture us, you with the waves", 500, 45},
        {"The ocean's colors on your face", 400, 50},
        {"I'll leave my heart with your air", 500, 40},
        {"So let me fly with you", 600, 30},
        {"Will you be forever with me?", 700, 50},
        {"", 300, 0},
        {"", 500, 60},
        {"My love will always stay by you", 700, 35},
        {"I'll keep it safe, so don't you worry a thing", 500, 40},
        {"I'll tell you I love you more", 600, 30},
        {"It's stuck with you forever, so promise you won't let it go", 500, 45},
        {"I'll trust the universe will always bring me to you", 700, 50},
        {"", 300, 0},
        {"", 500, 40},
        {"I'll imagine we fell in love", 700, 35},
        {"I'll nap under moonlight skies with you", 600, 30},
        {"I think I'll picture us, you with the waves", 500, 45},
        {"The ocean's colors on your face", 400, 50},
        {"I'll leave my heart with your air", 500, 40},
        {"So let me fly with you", 600, 30},
        {"Will you be forever with me?", 700, 50},
    };

    // Cetak lirik dengan huruf muncul satu per satu dengan delay yang berbeda
    for (const auto& baris : lirik) {
        const std::string& teks = std::get<0>(baris);
        int delayBaris = std::get<1>(baris);
        int delayHuruf = std::get<2>(baris);

        for (char c : teks) {
            std::cout << c << std::flush;
            std::this_thread::sleep_for(std::chrono::milliseconds(delayHuruf)); // Delay per huruf
        }
        std::cout << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(delayBaris)); // Delay setelah baris selesai
    }
}

int main() {
    // Panggil fungsi untuk mencetak lirik
    printLirik();
    return 0;
}
