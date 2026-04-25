import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SearchBarComponent } from './components/search-bar/search-bar';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, SearchBarComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {}