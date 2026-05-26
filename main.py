import pygame
import random
import math
import time

pygame.init()


class InfoDesenare:
    # Tema Premium "Sport Dashboard"
    CULOARE_FUNDAL = 20, 22, 26  # Negru-antracit mat
    PANEL_STATS = 35, 38, 45  # Gri inchis pentru caseta de stats
    LINIE_SEPARARE = 50, 55, 65  # Culoare pentru linia despartitoare
    TEXT_PRINCIPAL = 230, 230, 235  # Alb-murdar clar
    ACCENT_ALBASTRU = 20, 116, 225  # Le Mans Blue (aprins pt display)
    VERDE = 46, 204, 113  # Verde modern pt succes/comparatii
    ROSU = 231, 76, 60  # Rosu coral pt elemente active

    # Nuante metalice (Aluminium Glacier Silver)
    GRI_URI = [
        (160, 164, 170),
        (180, 184, 190),
        (200, 204, 210)
    ]

    # Fonturi moderne
    FONT_MIC = pygame.font.SysFont('segoeui', 17, bold=False)
    FONT_MARE = pygame.font.SysFont('segoeui', 28, bold=True)
    FONT_STATS = pygame.font.SysFont('consolas', 17, bold=True)

    PADDING_LATERAL = 100
    PADDING_SUS = 170  # Am marit putin sa incapa panelul

    def __init__(self, latime, inaltime, lista_numere):
        self.latime = latime
        self.inaltime = inaltime
        self.fereastra = pygame.display.set_mode((latime, inaltime))
        pygame.display.set_caption("Benchmark Sortare - Molnar si Roman (Anul 2)")
        self.setare_lista(lista_numere)

        self.comparatii = 0
        self.interschimbari = 0
        self.timp_start = 0
        self.timp_scurs = 0

    def setare_lista(self, lista_numere):
        self.lista = lista_numere
        self.val_min = min(lista_numere)
        self.val_max = max(lista_numere)

        self.latime_bloc = round((self.latime - self.PADDING_LATERAL) / len(lista_numere))
        self.inaltime_bloc = math.floor((self.inaltime - self.PADDING_SUS) / (self.val_max - self.val_min))
        self.start_x = self.PADDING_LATERAL // 2

        self.comparatii = 0
        self.interschimbari = 0
        self.timp_scurs = 0


def desenare_interfata(info, nume_algoritm, crescator):
    info.fereastra.fill(info.CULOARE_FUNDAL)

    # Titlu
    sens = "Crescator" if crescator else "Descrescator"
    titlu = info.FONT_MARE.render(f"{nume_algoritm} - {sens}", 1, info.ACCENT_ALBASTRU)
    info.fereastra.blit(titlu, (info.latime / 2 - titlu.get_width() / 2, 10))

    # Meniu
    controale = info.FONT_MIC.render("R - Reset | SPACE - Start | X - Exporta", 1, info.TEXT_PRINCIPAL)
    info.fereastra.blit(controale, (info.latime / 2 - controale.get_width() / 2, 48))

    sortari = info.FONT_MIC.render("B - Bubble | I - Insertion | S - Selection | Q - Quick", 1, info.TEXT_PRINCIPAL)
    info.fereastra.blit(sortari, (info.latime / 2 - sortari.get_width() / 2, 70))

    marime = info.FONT_MIC.render(f"SAGETI SUS/JOS - Marime (N={len(info.lista)}) | A/D - Sens", 1, info.TEXT_PRINCIPAL)
    info.fereastra.blit(marime, (info.latime / 2 - marime.get_width() / 2, 92))

    # Linie despartitoare fina (aer profi)
    pygame.draw.line(info.fereastra, info.LINIE_SEPARARE, (20, 120), (info.latime - 20, 120), 2)

    # Panel rotunjit pentru Stats
    latime_panel = 600
    inaltime_panel = 32
    x_panel = info.latime // 2 - latime_panel // 2
    y_panel = 130

    # Desenam backgroundul casetei de statistici (border_radius rotunjeste colturile)
    pygame.draw.rect(info.fereastra, info.PANEL_STATS, (x_panel, y_panel, latime_panel, inaltime_panel),
                     border_radius=8)

    # Textul din interiorul casetei
    text_stats = f" Timp: {info.timp_scurs:.4f}s  |  Comparatii: {info.comparatii}  |  Swaps: {info.interschimbari} "
    stats = info.FONT_STATS.render(text_stats, 1, info.VERDE)
    info.fereastra.blit(stats, (info.latime / 2 - stats.get_width() / 2, y_panel + 6))

    desenare_bare(info)
    pygame.display.update()


def desenare_bare(info, pozitii_colorate={}, curata_fundal=False):
    lista = info.lista

    if curata_fundal:
        # Curatam zona graficului
        zona_curatare = (info.PADDING_LATERAL // 2, info.PADDING_SUS,
                         info.latime - info.PADDING_LATERAL, info.inaltime - info.PADDING_SUS)
        pygame.draw.rect(info.fereastra, info.CULOARE_FUNDAL, zona_curatare)

        # Redesenam strict Panel-ul de Stats cand se updateaza datele live
        latime_panel = 600
        inaltime_panel = 32
        x_panel = info.latime // 2 - latime_panel // 2
        y_panel = 130

        pygame.draw.rect(info.fereastra, info.PANEL_STATS, (x_panel, y_panel, latime_panel, inaltime_panel),
                         border_radius=8)
        text_stats = f" Timp: {info.timp_scurs:.4f}s  |  Comparatii: {info.comparatii}  |  Swaps: {info.interschimbari} "
        stats = info.FONT_STATS.render(text_stats, 1, info.VERDE)
        info.fereastra.blit(stats, (info.latime / 2 - stats.get_width() / 2, y_panel + 6))

    for i, valoare in enumerate(lista):
        x = info.start_x + i * info.latime_bloc
        y = info.inaltime - (valoare - info.val_min) * info.inaltime_bloc
        culoare = info.GRI_URI[i % 3]

        if i in pozitii_colorate:
            culoare = pozitii_colorate[i]

        # TRUC PREMIUM: Scadem 1 pixel din latime ca sa cream un mic spatiu/gap intre bare
        latime_bara_vizuala = info.latime_bloc - 1 if info.latime_bloc > 1 else 1

        pygame.draw.rect(info.fereastra, culoare, (x, y, latime_bara_vizuala, info.inaltime))

    if curata_fundal:
        pygame.display.update()


# --- ALGORITMI DE SORTARE ---

def bubble_sort(info, crescator=True):
    lista = info.lista
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            numar1 = lista[j]
            numar2 = lista[j + 1]
            info.comparatii += 1

            if (numar1 > numar2 and crescator) or (numar1 < numar2 and not crescator):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                info.interschimbari += 1
                desenare_bare(info, {j: info.VERDE, j + 1: info.ROSU}, True)
                yield True
    return lista


def insertion_sort(info, crescator=True):
    lista = info.lista
    for i in range(1, len(lista)):
        curent = lista[i]
        while True:
            info.comparatii += 1
            ascendent_ok = i > 0 and lista[i - 1] > curent and crescator
            descendent_ok = i > 0 and lista[i - 1] < curent and not crescator

            if not ascendent_ok and not descendent_ok:
                break

            lista[i] = lista[i - 1]
            i -= 1
            lista[i] = curent
            info.interschimbari += 1

            desenare_bare(info, {i - 1: info.VERDE, i: info.ROSU}, True)
            yield True
    return lista


def selection_sort(info, crescator=True):
    lista = info.lista
    for i in range(len(lista)):
        idx_extrem = i
        for j in range(i + 1, len(lista)):
            info.comparatii += 1
            if (lista[j] < lista[idx_extrem] and crescator) or (lista[j] > lista[idx_extrem] and not crescator):
                idx_extrem = j

        info.interschimbari += 1
        lista[i], lista[idx_extrem] = lista[idx_extrem], lista[i]

        desenare_bare(info, {i: info.VERDE, idx_extrem: info.ROSU}, True)
        yield True
    return lista


def quick_sort_recursiv(info, stanga, dreapta, crescator=True):
    if stanga < dreapta:
        pivot = info.lista[dreapta]
        i = stanga - 1

        for j in range(stanga, dreapta):
            info.comparatii += 1
            if (info.lista[j] < pivot and crescator) or (info.lista[j] > pivot and not crescator):
                i += 1
                info.lista[i], info.lista[j] = info.lista[j], info.lista[i]
                info.interschimbari += 1
                desenare_bare(info, {i: info.VERDE, j: info.ROSU}, True)
                yield True

        info.lista[i + 1], info.lista[dreapta] = info.lista[dreapta], info.lista[i + 1]
        info.interschimbari += 1
        desenare_bare(info, {i + 1: info.VERDE, dreapta: info.ROSU}, True)
        yield True

        pivot_index = i + 1
        yield from quick_sort_recursiv(info, stanga, pivot_index - 1, crescator)
        yield from quick_sort_recursiv(info, pivot_index + 1, dreapta, crescator)


def wrapper_quick_sort(info, crescator=True):
    yield from quick_sort_recursiv(info, 0, len(info.lista) - 1, crescator)


def generare_lista_start(n, val_min, val_max):
    lista_noua = []
    for _ in range(n):
        lista_noua.append(random.randint(val_min, val_max))
    return lista_noua


def main():
    ruleaza = True
    ceas = pygame.time.Clock()

    n = 50
    val_min = 0
    val_max = 100

    lista = generare_lista_start(n, val_min, val_max)
    info = InfoDesenare(800, 600, lista)

    sortare = False
    crescator = True
    algoritm_sortare = bubble_sort
    nume_algoritm = "Bubble Sort"
    generator_sortare = None

    pygame.mixer.init()
    try:
        sunet = pygame.mixer.Sound("click.wav")
        sunet.set_volume(0.3)
    except FileNotFoundError:
        print("Atentie: Fisierul click.wav lipseste din folder!")

    while ruleaza:
        ceas.tick(60)

        if sortare:
            info.timp_scurs = time.time() - info.timp_start
            try:
                next(generator_sortare)
            except StopIteration:
                sortare = False
        else:
            desenare_interfata(info, nume_algoritm, crescator)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ruleaza = False

            if event.type == pygame.KEYDOWN:
                taste_valide = [pygame.K_r, pygame.K_SPACE, pygame.K_a, pygame.K_d,
                                pygame.K_b, pygame.K_i, pygame.K_q, pygame.K_s,
                                pygame.K_x, pygame.K_UP, pygame.K_DOWN]
                if event.key in taste_valide:
                    try:
                        sunet.play()
                    except:
                        pass

                if event.key == pygame.K_r:
                    lista = generare_lista_start(n, val_min, val_max)
                    info.setare_lista(lista)
                    sortare = False

                elif event.key == pygame.K_SPACE and not sortare:
                    sortare = True
                    info.comparatii = 0
                    info.interschimbari = 0
                    info.timp_start = time.time()
                    generator_sortare = algoritm_sortare(info, crescator)

                elif event.key == pygame.K_x and not sortare:
                    if info.timp_scurs > 0:
                        try:
                            with open("rezultate_benchmark.txt", "a") as f:
                                sens = "Cresc" if crescator else "Desc"
                                timestamp = time.strftime('%d-%m-%Y %H:%M')
                                f.write(
                                    f"[{timestamp}] {nume_algoritm} | N={n} | {sens} | Timp: {info.timp_scurs:.4f}s | Comp: {info.comparatii} | Swaps: {info.interschimbari}\n")
                            print(f"Salvat cu succes in rezultate_benchmark.txt!")
                        except Exception as e:
                            print(f"Eroare la salvare: {e}")

                elif event.key == pygame.K_a and not sortare:
                    crescator = True
                elif event.key == pygame.K_d and not sortare:
                    crescator = False

                elif event.key == pygame.K_b and not sortare:
                    algoritm_sortare = bubble_sort
                    nume_algoritm = "Bubble Sort"
                elif event.key == pygame.K_i and not sortare:
                    algoritm_sortare = insertion_sort
                    nume_algoritm = "Insertion Sort"
                elif event.key == pygame.K_q and not sortare:
                    algoritm_sortare = wrapper_quick_sort
                    nume_algoritm = "Quick Sort"
                elif event.key == pygame.K_s and not sortare:
                    algoritm_sortare = selection_sort
                    nume_algoritm = "Selection Sort"

                elif event.key == pygame.K_UP and not sortare:
                    n = min(150, n + 10)
                    lista = generare_lista_start(n, val_min, val_max)
                    info.setare_lista(lista)
                elif event.key == pygame.K_DOWN and not sortare:
                    n = max(10, n - 10)
                    lista = generare_lista_start(n, val_min, val_max)
                    info.setare_lista(lista)

    pygame.quit()


if __name__ == "__main__":
    main()