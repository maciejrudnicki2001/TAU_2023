import org.example.PokeApi;
import org.junit.Assert;
import org.junit.Test;
import org.junit.jupiter.api.Assertions;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class PokeApiTests {
    PokeApi pokeApi = new PokeApi();

    String url = "https://pokeapi.co/api/v2/";
    @Test
    public void testGetInfo() {
        String url = "https://pokeapi.co/api/v2/pokemon/1/";
        String expected = "https://pokeapi.co/api/v2/pokemon/1/";
        String actual = pokeApi.getInfo(url);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testGetInfoMock() {
        PokeApi pokeApi = mock(PokeApi.class);
        String url = "https://pokeapi.co/api/v2/pokemon/1/";
        String expected = "https://pokeapi.co/api/v2/pokemon/1/";
        when(pokeApi.getInfo(url)).thenReturn(expected);
        String actual = pokeApi.getInfo(url);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testGetInfoAboutEvolutionChain() {
        PokeApi pokeApi = mock(PokeApi.class);
        String expect = "{\"baby_trigger_item\":null,\"chain\":{\"evolution_details\":" +
                "[{\"gender\":null,\"held_item\":null,\"item\":null,\"known_move\":null,\"" +
                "known_move_type\":null,\"location\":null,\"min_affection\":null,\"min_beauty\"" +
                ":null,\"min_happiness\":null,\"min_level\":16,\"needs_overworld_rain\":false,\"" +
                "party_species\":null,\"party_type\":null,\"relative_physical_stats\":null,\"time_of_day\"" +
                ":\"day\",\"trade_species\":null,\"trigger\":{\"name\":\"level-up\",\"url\":" +
                "\"https://pokeapi.co/api/v2/evolution-trigger/1/\"},\"turn_upside_down\":false}]," +
                "\"evolves_to\":[{\"evolution_details\":[{\"gender\":null,\"held_item\":null,\"item\"" +
                ":null,\"known_move\":null,\"known_move_type\":null,\"location\":null,\"min_affection\"" +
                ":null,\"min_beauty\":null,\"min_happiness\":null,\"min_level\":32,\"needs_overworld_rain\"" +
                ":false,\"party_species\":null,\"party_type\":null,\"relative_physical_stats\":null,\"time_of_day\"" +
                ":\"day\",\"trade_species\":null,\"trigger\":{\"name\":\"level-up\",\"url\":\"https://pokeapi.co/api/v2/evolution-trigger/1/\"}" +
                ",\"turn_upside_down\":false}],\"evolves_to\":[],\"is_baby\":false,\"species\":{\"name\":\"venusaur\",\"url" +
                "\":\"https://pokeapi.co/api/v2/pokemon-species/3/\"}}],\"is_baby\":false,\"species\":{\"name\":\"bulbasaur\",\"url" +
                "\":\"https://pokeapi.co/api/v2/pokemon-species/1/\"}}}";
        when(pokeApi.getInfo(url + "evolution-chain/3/")).thenReturn(expect);
        String info = pokeApi.getInfo(url + "evolution-chain/3/");
        Assertions.assertEquals(info, expect);
    }

    @Test
    public void testGetInfoAboutEvolutionTrigger() {
        PokeApi pokeApi = mock(PokeApi.class);
        when(pokeApi.getInfo(url + "evolution-trigger/1/")).thenReturn(
                "{\"id\":1,\"name\":\"level-up\",\"names\":[{\"language\":{\"name\":\"en\",\"url\":\"https://pokeapi.co/api/v2/language/9/\"},\"name\":\"Level up\"}],\"pokemon_species\":[{\"name\":\"bulbasaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/1/\"},{\"name\":\"ivysaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/2/\"},{\"name\":\"venusaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/3/\"},{\"name\":\"charmander\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/4/\"},{\"name\":\"charmeleon\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/5/\"},{\"name\":\"charizard\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/6/\"},{\"name\":\"squirtle\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/7/\"},{\"name\":\"wartortle\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/8/\"},{\"name\":\"blastoise\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/9/\"}]}");
        String info = pokeApi.getInfo(url + "evolution-trigger/1/");
        Assertions.assertEquals(info, "{\"id\":1,\"name\":\"level-up\",\"names\":[{\"language\":{\"name\":\"en\",\"url\":\"https://pokeapi.co/api/v2/language/9/\"},\"name\":\"Level up\"}],\"pokemon_species\":[{\"name\":\"bulbasaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/1/\"},{\"name\":\"ivysaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/2/\"},{\"name\":\"venusaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/3/\"},{\"name\":\"charmander\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/4/\"},{\"name\":\"charmeleon\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/5/\"},{\"name\":\"charizard\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/6/\"},{\"name\":\"squirtle\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/7/\"},{\"name\":\"wartortle\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/8/\"},{\"name\":\"blastoise\",\"url\":\"https://pokeapi.co/api/v2/pokemon-species/9/\"}]}");

}
}

