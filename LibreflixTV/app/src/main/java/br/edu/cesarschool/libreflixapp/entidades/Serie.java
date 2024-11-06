package br.edu.cesarschool.libreflixapp.entidades;

import java.time.LocalDate;

public class Serie extends Obra {
    public int qntEpisodios;
    public Episodio[] episodios;

    public Serie(int id, String titulo, String descricacao, LocalDate dataLancamento, String diretor,
                 boolean isPopular, boolean isDestaque, boolean isNovo, Generos[] generos, Episodio[] episodios) {
        super(id, titulo, descricacao, dataLancamento, diretor, isPopular, isDestaque, isNovo, generos);
        this.episodios = episodios;
        this.qntEpisodios = episodios.length;
    }

    public int getQntEpisodios() {
        return qntEpisodios;
    }

    public Episodio[] getEpisodios() {
        return episodios;
    }

    public void addEpisode(Episodio episode, int duracao) {
        Episodio[] newEpisodes = new Episodio[episodios.length + 1];

        for(int i = 0; i < episodios.length; i++) {
            newEpisodes[i] = episodios[i];
        }
        newEpisodes[episodios.length] = episode;
        episodios = newEpisodes;
        qntEpisodios++;
    }
}
