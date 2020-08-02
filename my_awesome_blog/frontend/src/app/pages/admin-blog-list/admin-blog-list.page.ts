import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { NawahService, Res, Doc } from 'ng-nawah';


@Component({
  selector: 'page-admin-blog-list',
  templateUrl: 'admin-blog-list.page.html',
})
export class AdminBlogListPage implements OnInit {

  blogs: Array<Doc> = [];

  constructor(private nawah: NawahService) { }

  ngOnInit() {
    this.readPosts();
  }

  readPosts(): void {
    this.nawah.call({endpoint: 'blog/read'}).subscribe({
      next: (res) => {
        this.blogs = res.args.docs;
      },
      error: (err: Res<Doc>) => {
        alert(`Unexpected error occurred: ${err.msg || err}`);
      }
    });
  }

  deletePost(_id: string): void {
    if (confirm('Are you sure you want to delete this blog post?')) {
      this.nawah.call({
        endpoint: 'blog/delete',
        query: [{
          _id: _id
        }]
      }).subscribe({
        next: () => {
          this.readPosts();
        },
        error: (err: Res<Doc>) => {
          alert(`Unexpected error occurred: ${err.msg || err}`);
        }
      });
    }
  }

}