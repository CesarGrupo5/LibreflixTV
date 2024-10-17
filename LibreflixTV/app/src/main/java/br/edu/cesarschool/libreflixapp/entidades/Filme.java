package br.edu.cesarschool.libreflixapp.entidades;

import java.time.LocalDate;

public class Filme extends Obra {
    private int duracao;

    public Filme(int id, String titulo, String descricacao, LocalDate dataLancamento, String diretor, boolean isPopular, boolean isDestaque, boolean isNovo, Generos[] generos, int duracao) {
        super(id, titulo, descricacao, dataLancamento, diretor, isPopular, isDestaque, isNovo, generos);
        this.duracao = duracao;
    }

    public int getDuracao() {
        return duracao;
    }
}
