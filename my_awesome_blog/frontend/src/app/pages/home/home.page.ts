import { Component } from '@angular/core';
import { Observable } from 'rxjs';

import { NawahService, Res } from 'ng-nawah';

@Component({
  selector: 'page-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.css'],
})
export class HomePage {

  blogs$: Observable<Res<any>> = this.nawah.call({
    endpoint: 'blog/read'
  });

  comments$: {
    [key: string]: Observable<Res<any>>
  } = {}

  constructor(private nawah: NawahService) { }

  loadComments(blog_id: string): void { 
    this.comments$[blog_id] = this.nawah.call({
      endpoint: 'blog_comment/read',
      query: [{ blog: blog_id }]
    });
  }

}